from PIL import Image

def images_to_pdf(image_paths, pdf_path):
    images = []
    
    # 读取所有图片并转换为RGB模式
    for image_path in image_paths:
        image = Image.open(image_path)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        images.append(image)
    
    # 保存为PDF（多张图片合并为一个PDF）
    images[0].save(pdf_path, save_all=True, append_images=images[1:], resolution=100.0, quality=95)

# 示例使用
image_paths = ['1.jpg', '2.jpg']  # 多张图片的路径
pdf_path = 'output.pdf'  # 输出的PDF路径

images_to_pdf(image_paths, pdf_path)

print(f'PDF已保存为 {pdf_path}')
