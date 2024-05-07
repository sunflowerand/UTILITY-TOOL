"""
@Author: sunflowerand
@Time: 2024/05/07
"""
import os
import shutil
import logging 
import sys

logging.basicConfig(
    level=logging.DEBUG,  
    format='%(asctime)s - %(levelname)s - %(message)s',  
    datefmt='%Y-%m-%d %H:%M:%S',  
    filename='app.log',  
    filemode='w'  # 文件模式，'w'表示每次运行都清空日志重新写入，'a'表示追加到文件末尾
)

logger = logging.getLogger(__name__)

def copy_file(src_path, dest_path):
    """
    复制文件到指定目录
    src_path:源文件路径
    dest_path:目标路径
    """
    try:
        shutil.copy2(src_path, dest_path)
        logger.info(f"'{src_path}' to '{dest_path}' successful")
    except:
        logger.info(f"'{src_path}' to '{dest_path}'")
        logger.error("copy failed!")

def copy_all_files(dest_path, dir_path=os.getcwd()):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if(file != 'app.log' and file != os.path.basename(__file__)):
                full_path = os.path.join(root, file)
                copy_file(full_path, dest_path)


new_dir_name = "all_files"
new_dir_name = input("please enter the name directory will be named")

current_dir = os.getcwd()
try:
    new_dir_path = os.path.join(current_dir, new_dir_name)
except:
    logger.error("the Filename is illegal")
    sys.exit(0)


try: 
    os.mkdir(new_dir_path)
except:
    logger.error("create folder filed")
    exit(0)


copy_all_files(new_dir_path)