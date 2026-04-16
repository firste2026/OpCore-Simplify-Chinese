from Scripts import resource_fetcher
from Scripts import github
from Scripts import run
from Scripts import utils
import os
import tempfile
import shutil

class Updater:
    def __init__(self):
        self.github = github.Github()
        self.fetcher = resource_fetcher.ResourceFetcher()
        self.run = run.Run().run
        self.utils = utils.Utils()
        self.sha_version = os.path.join(os.path.dirname(os.path.realpath(__file__)), "sha_version.txt")
        self.download_repo_url = "https://github.com/lzhoang2801/OpCore-Simplify/archive/refs/heads/main.zip"
        self.temporary_dir = tempfile.mkdtemp()
        self.current_step = 0

    def get_current_sha_version(self):
        print("正在检查当前版本...")
        try:
            current_sha_version = self.utils.read_file(self.sha_version)

            if not current_sha_version:
                print("SHA 版本信息缺失。")
                return "missing_sha_version"

            return current_sha_version.decode()
        except Exception as e:
            print("读取当前 SHA 版本时出错：{}".format(str(e)))
            return "error_reading_sha_version"

    def get_latest_sha_version(self):
        print("正在从 GitHub 获取最新版本...")
        try:
            commits = self.github.get_commits("lzhoang2801", "OpCore-Simplify")
            return commits["commitGroups"][0]["commits"][0]["oid"]
        except Exception as e:
            print("获取最新 SHA 版本时出错：{}".format(str(e)))
        
        return None

    def download_update(self):
        self.current_step += 1
        print("")
        print("步骤 {}: 正在创建临时目录...".format(self.current_step))
        try:
            self.utils.create_folder(self.temporary_dir)
            print("  临时目录已创建。")
            
            self.current_step += 1
            print("步骤 {}: 正在下载更新包...".format(self.current_step))
            print("  ", end="")
            file_path = os.path.join(self.temporary_dir, os.path.basename(self.download_repo_url))
            self.fetcher.download_and_save_file(self.download_repo_url, file_path)
            
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                print("  更新包已下载 ({:.1f} KB)".format(os.path.getsize(file_path)/1024))
                
                self.current_step += 1
                print("步骤 {}: 正在解压文件...".format(self.current_step))
                self.utils.extract_zip_file(file_path)
                print("  文件解压成功")
                return True
            else:
                print("  下载失败或文件为空")
                return False
        except Exception as e:
            print("  下载/解压过程中出错：{}".format(str(e)))
            return False

    def update_files(self):
        self.current_step += 1
        print("步骤 {}: 正在更新文件...".format(self.current_step))
        try:
            target_dir = os.path.join(self.temporary_dir, "OpCore-Simplify-main")
            if not os.path.exists(target_dir):
                target_dir = os.path.join(self.temporary_dir, "main", "OpCore-Simplify-main")
                
            if not os.path.exists(target_dir):
                print("  找不到解压后的文件目录")
                return False
                
            file_paths = self.utils.find_matching_paths(target_dir, type_filter="file")
            
            total_files = len(file_paths)
            print("  找到 {} 个文件待更新".format(total_files))
            
            updated_count = 0
            for index, (path, type) in enumerate(file_paths, start=1):
                source = os.path.join(target_dir, path)
                destination = source.replace(target_dir, os.path.dirname(os.path.realpath(__file__)))
                
                self.utils.create_folder(os.path.dirname(destination))
                
                print("    正在更新 [{}/{}]: {}".format(index, total_files, os.path.basename(path)), end="\r")
                
                try:
                    shutil.move(source, destination)
                    updated_count += 1
                    
                    if ".command"  in os.path.splitext(path)[-1] and os.name != "nt":
                        self.run({
                            "args": ["chmod", "+x", destination]
                        })
                except Exception as e:
                    print("      更新失败 {}: {}".format(path, str(e)))
            
            print("")
            print("  成功更新 {}/{} 个文件".format(updated_count, total_files))
            
            self.current_step += 1
            print("步骤 {}: 正在清理临时文件...".format(self.current_step))
            shutil.rmtree(self.temporary_dir)
            print("  清理完成")
            
            return True
        except Exception as e:
            print("  文件更新过程中出错：{}".format(str(e)))
            return False

    def save_latest_sha_version(self, latest_sha):
        try:
            self.utils.write_file(self.sha_version, latest_sha.encode())
            self.current_step += 1
            print("步骤 {}: 版本信息已更新。".format(self.current_step))
            return True
        except Exception as e:
            print("保存版本信息失败：{}".format(str(e)))
            return False

    def run_update(self):
        self.utils.head("检查更新")
        print("")
        
        current_sha_version = self.get_current_sha_version()
        latest_sha_version = self.get_latest_sha_version()
        
        print("")

        if latest_sha_version is None:
            print("无法从 GitHub 验证最新版本。")
            print("当前脚本 SHA 版本：{}".format(current_sha_version))
            print("请检查您的网络连接并稍后重试。")
            print("")
            
            while True:
                user_input = self.utils.request_input("您想跳过更新过程吗？(是/否): ").strip().lower()
                if user_input in ("是", "yes"):
                    print("")
                    print("更新过程已跳过。")
                    return False
                elif user_input in ("否", "no"):
                    print("")
                    print("使用默认版本检查继续更新...")
                    latest_sha_version = "update_forced_by_user"
                    break
                else:
                    print("\033[91m无效选择，请重试。\033[0m\n\n")
        else:
            print("当前脚本 SHA 版本：{}".format(current_sha_version))
            print("最新脚本 SHA 版本：{}".format(latest_sha_version))
        
        print("")
        
        if latest_sha_version != current_sha_version:
            print("有可用更新！")
            print("正在从版本 {} 更新到 {}".format(current_sha_version, latest_sha_version))
            print("")
            print("正在开始更新过程...")
            
            if not self.download_update():
                print("")
                print("  更新失败：无法下载或解压更新包")

                if os.path.exists(self.temporary_dir):
                    self.current_step += 1
                    print("步骤 {}: 正在清理临时文件...".format(self.current_step))
                    shutil.rmtree(self.temporary_dir)
                    print("  清理完成")

                return False
                
            if not self.update_files():
                print("")
                print("  更新失败：无法更新文件")
                return False
                
            if not self.save_latest_sha_version(latest_sha_version):
                print("")
                print("  更新已完成但版本信息无法保存")
            
            print("")
            print("更新成功完成！")
            print("")
            print("程序需要重新启动以完成更新过程。")
            return True
        else:
            print("您已在使用最新版本")
            return False