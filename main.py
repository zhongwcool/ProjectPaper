import os
import shutil
from pathlib import Path


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # 获取当前用户的图片文件夹路径
    pictures_dir = Path(os.getcwd())

    # Windows Spotlight 图片所在的目录
    spotlight_path = os.path.join(os.getenv('LOCALAPPDATA'),
                                  'Packages',
                                  'Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy',
                                  'LocalState', 'Assets')

    # 导出 Spotlight 图片的目标文件夹
    export_folder = pictures_dir / "Spotlight"
    export_folder.mkdir(exist_ok=True)

    image_count = 0  # Initialize the counter

    # 复制并重命名图片
    for filename in os.listdir(spotlight_path):
        # 构建完整的文件路径
        source_file = os.path.join(spotlight_path, filename)

        # 简单的过滤，通过文件大小过滤非图片内容（这里设定图片至少为 100KB）
        if os.path.getsize(source_file) > 100 * 1024:
            target_file = export_folder / (filename + ".jpg")

            # 如果存在命名冲突，不重复复制
            if not target_file.exists():
                shutil.copy2(source_file, target_file)
                relative_target_file = os.path.relpath(target_file, pictures_dir)
                print(f"新文件: {relative_target_file}")
                image_count += 1  # Increment the counter

    print(f"{image_count} images have been exported to: {export_folder}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user_name = os.getlogin()
    print_hi(user_name)
    input("按任意键退出...")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
