import ascii_magic
import argparse
try:
    parser = argparse.ArgumentParser()
    parser.add_argument('p', help='Masukan path gambarnya bro !', type=str)

    arg = parser.parse_args()
    path = arg.p

    my_art = ascii_magic.from_image_file(path)
    ascii_magic.to_terminal(my_art)
except Exception as e:
    print('Error Bos !', e)


# import ascii_magic
# try:
#     my_art = ascii_magic.from_image_file('img/uchiha.jpg')
#     ascii_magic.to_terminal(my_art)
# except Exception as e:
#     print('Error Bos !', e)
