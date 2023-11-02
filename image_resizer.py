import sys
from PIL import Image, UnidentifiedImageError

def resize_and_fill(input_image_path, output_image_path, target_width=405, target_height=720):
    try:
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
        
    except FileNotFoundError:
        print(f"Error: The file {input_image_path} was not found. Please check the filename.")
    except UnidentifiedImageError:
        print(f"Error: The file {input_image_path} is not a recognized image file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    for input_image_path in sys.argv[1:]:
        try:
            # 确保文件路径没有引号
            input_image_path = input_image_path.replace('\"', '').replace("\'", "")
            
            # 生成输出文件路径
            parts = input_image_path.rsplit('.', 1)
            if len(parts) < 2 or not parts[1].lower() in ['jpg', 'jpeg', 'png', 'bmp', 'gif']:
                raise ValueError(f"Unsupported file extension for file: {input_image_path}")
            output_image_path = f"{parts[0]}_resized.{parts[1]}"
            
            # 处理图片
            resize_and_fill(input_image_path, output_image_path)
            print(f"Processed {input_image_path} and saved as {output_image_path}")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred while processing {input_image_path}: {e}")



'''
@echo off
python "C:\ImageScripts\demo.py" %*
echo.
echo Process completed. Press any key to exit.
pause > nul

'''