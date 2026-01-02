import os
import PyInstaller.__main__
import osam
import onnxruntime

# 1. 获取 osam 库的安装路径 (自动解决路径问题)
OSAM_PATH = os.path.dirname(osam.__file__)
print(f"Found osam path: {OSAM_PATH}")

LABELME_PATH='./labelme'

# 2. 定义分隔符 (Windows 必须用分号)
sep = ';' if os.name == 'nt' else ':'

print(f'--add-data=./labelme/config/default_config.yaml{sep}labelme/config')
# 3. 构造打包参数
opts = [
    './labelme/__main__.py',             # 入口文件
    '--name=LabelMe_Custom',           # exe名字
    '--windowed',
    '--noconfirm',
    # '--specpath=build',
    f'--add-data={os.path.join(OSAM_PATH, "_models/yoloworld/clip/bpe_simple_vocab_16e6.txt.gz")}{sep}osam/_models/yoloworld/clip',
    f'--add-data=./labelme/config/default_config.yaml{sep}labelme/config',
    f'--add-data=./labelme/icons/*{sep}labelme/icons',
    f'--add-data=./labelme/translate/*{sep}translate',
    f'--icon=./labelme/icons/icon-256.png',
    '--onefile'
]

# 4. 执行打包
print("Starting PyInstaller...")
PyInstaller.__main__.run(opts)