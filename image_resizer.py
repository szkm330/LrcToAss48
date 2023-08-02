import sys
from PIL import Image, ImageOps

def resize_and_fill(input_image_path, output_image_path, target_width=405, target_height=720):
    # 打开原始图片
    original_image = Image.open(input_image_path)
    
    # 获取原始图片的宽高
    original_width, original_height = original_image.size
    
    # 计算宽高缩放比例
    width_ratio = target_width / original_width
    height_ratio = target_height / original_height
    scale_ratio = min(width_ratio, height_ratio)
    
    # 计算调整后的宽高
    new_width = int(original_width * scale_ratio)
    new_height = int(original_height * scale_ratio)
    
    # 缩放图片并居中
    resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)
    offset_x = (target_width - new_width) // 2
    offset_y = (target_height - new_height) // 2
    new_image = Image.new("RGB", (target_width, target_height), color="black")
    new_image.paste(resized_image, (offset_x, offset_y))
    
    # 保存输出图片
    new_image.save(output_image_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python demo.py input_image_path output_image_path")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]

    resize_and_fill(input_image_path, output_image_path)
