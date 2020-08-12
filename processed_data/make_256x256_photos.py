def resize(image):
    import cv2
    from math import ceil
    height=256
    image=as_rgb_image(image)
    image=as_byte_image(image)
    width=ceil(height/get_image_height(image)*get_image_width(image))
    image=cv2.resize(image,(width,height))
    return image

def pad_and_crop(image):
    width=256
    image=bordered_image_solid_color(image,thickness=0,width=width)
    x_origin=(get_image_width(image)-width)//2
    image=image[:,x_origin:x_origin+width]
    image=as_rgb_image(image)
    image=as_byte_image(image)
    return image

image_paths=get_all_paths('../raw_data/good_images')
images=load_images(image_paths,show_progress=True)
images_resized=[pad_and_crop(resize(image)) for image in images]

output_directory='photos_256x256'
make_directory(output_directory)
images_resized_paths=[path_join(output_directory, get_file_name(image_path)) for image_path in image_paths]
save_images(images_resized, images_resized_paths, show_progress=True)