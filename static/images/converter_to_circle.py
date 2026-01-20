from PIL import Image, ImageDraw, ImageOps
import os

# --- 配置 ---
# 输入文件：你现在的方形图片
input_path = "favicon.png"
# 输出文件：即将生成的圆形图片
output_path = "favicon_circle.png"

def create_circular_favicon(input_file, output_file):
    # 1. 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"❌ 错误：找不到文件 '{input_file}'")
        print("请确保 static/head.png 存在。")
        return

    try:
        # 2. 打开图片并转换为 RGBA 模式 (A=Alpha透明通道)
        img = Image.open(input_file).convert("RGBA")
        
        # 确保图片是正方形，如果不是，取最短边裁剪成正方形
        min_size = min(img.size)
        img = ImageOps.fit(img, (min_size, min_size), centering=(0.5, 0.5))
        size = img.size

        # 3. 创建一个遮罩 (Mask)
        # 遮罩是一个全黑的图片 (L模式)
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        # 在遮罩上画一个全白的圆。为了抗锯齿平滑，边缘退缩1个像素。
        draw.ellipse((1, 1, size[0]-2, size[1]-2), fill=255)

        # 4. 将这个圆形遮罩应用到原图的 Alpha 通道
        # 遮罩黑色的地方变透明，白色的地方保留原图
        img.putalpha(mask)

        # 5. 保存结果
        img.save(output_file, "PNG")
        print(f"✅ 成功！圆形图标已生成: {output_file}")
        print("现在请去修改 hugo.yaml 配置文件。")

    except Exception as e:
        print(f"❌ 处理出错: {e}")

if __name__ == "__main__":
    create_circular_favicon(input_path, output_path)