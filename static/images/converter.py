from PIL import Image
import os

# --- 配置区 ---
input_file = "head.jpg"  # 你之前的 jpg 文件名，如果没有就改成你现在的照片名
output_favicon = "favicon.png"          # 输出：浏览器标签页图标
output_apple = "apple-touch-icon.png"   # 输出：苹果/安卓主屏图标

# 定义尺寸
SIZE_FAVICON = (32, 32)    # 标准 Favicon 尺寸
SIZE_APPLE = (180, 180)    # 标准 Apple Touch Icon 尺寸

def create_logo(input_path):
    # 1. 检查文件是否存在
    if not os.path.exists(input_path):
        print(f"❌ 错误：找不到文件 '{input_path}'")
        print("请确保你把照片放在脚本同级目录，并修改代码中的 'input_file' 变量。")
        return

    try:
        # 2. 打开图片
        img = Image.open(input_path)
        print(f"✅ 已打开图片: {input_path} (尺寸: {img.size})")

        # 3. 生成 Favicon (32x32)
        # 使用 LANCZOS 算法进行高质量缩放
        favicon = img.resize(SIZE_FAVICON, Image.Resampling.LANCZOS)
        favicon.save(output_favicon, "PNG")
        print(f"✅ 已生成 Favicon: {output_favicon} (32x32)")

        # 4. 生成 Apple Touch Icon (180x180)
        apple_icon = img.resize(SIZE_APPLE, Image.Resampling.LANCZOS)
        apple_icon.save(output_apple, "PNG")
        print(f"✅ 已生成 Apple Icon: {output_apple} (180x180)")

        print("-" * 30)
        print("🚀 完成！请执行以下操作：")
        print(f"请将 {output_favicon} 和 {output_apple} 移动到你的 hugo/MyFreshWebsite/static/ 目录下。")

    except Exception as e:
        print(f"❌ 处理过程中出错: {e}")

if __name__ == "__main__":
    create_logo(input_file)