import argparse
import markdown2

header = '''
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset='utf-8'/>
    <link rel='stylesheet' type='text/css' href='main.css'/>
    <link href='https://fonts.googleapis.com/css?family=Roboto'rel='stylesheet'>
    <style>body {font-family: 'Roboto', sans-serif;}</style></head>
    <body>
    </body>

    </html>
    '''
def convert_md_to_Html(md_file, html_file):
    file_open = open(md_file, "r", encoding="utf-8")
    file_to_convert = file_open.read()
    html = markdown2.markdown(file_to_convert)
    new_file = open(html_file, "w",encoding="utf-8")
    new_file.write(header + html) 
    new_file.close()
    print('Conversion du fichier md en Html réussi.')

def convert_md_to_Html_for_german(md_file, html_file):
    file_open = open(md_file, "r",encoding="utf-8")
    file_to_convert = file_open.read()
    html = markdown2.markdown(file_to_convert)
    output_file = open(html_file, "w",encoding="utf-8")
    output_file.write(html) 
    output_file.close()
    file_already_change = open(html_file, "r",encoding="utf-8")
    file_for_replace = file_already_change.read()
    new_file = open(html_file, "w",encoding="utf-8")
    file_for_german = file_for_replace.replace("ss", "z").replace("s", "z").replace("qu", "k").replace("ce", "ze").replace("c", "k").replace("ç", "z").replace("ph", "f").replace("pp", "p").replace("gu", "ch").replace("g", "ch").replace("j", "k").replace("v", "f").replace("s", "").replace("mm","m")
    new_file.write(file_for_german)
    new_file.close()
    print("Conversion du fichier md en Html réussi en allemand.")

def convert_md_to_Html_with_kikoo(md_file, html_file):
    file_open = open(md_file, "r",encoding="utf-8")
    file_to_convert = file_open.read()
    html = markdown2.markdown(file_to_convert)
    new_file = open(html_file, "w",encoding="utf-8")
    new_file.write(html) 
    new_file.close()
    file_with_kikoo = open(html_file, "w", encoding="utf-8")
    append_kikoo = "<p>Kikoo</p>"
    file_with_kikoo.write(html + append_kikoo)
    file_with_kikoo.close()
    print("Conversion du fichier md en Html réussi, et ajout de kikoo à la fin.")

parser = argparse.ArgumentParser()
parser.add_argument("-i", '--input',help='Cette option te permettras de choisir le fichier que tu veux lire.')
parser.add_argument("-o", '--output',help='Cette option te permettras de mettre les changements éffectués sur un autre fichier.')
parser.add_argument("-a", '--achtung',help='Si tu rajoutes cette option cela convertiras en allemand aussi.', action="store_true")
parser.add_argument("-k", '--kikoo',help="Si tu rajoutes cette option cela ajoutera kikoo à la fin du texte", action="store_true")
args = parser.parse_args()

if args.achtung == True:
    print('Conversion en cours...')
    convert_md_to_Html_for_german(args.input,args.output)
elif args.kikoo == True:
    print('Conversion en cours...')
    convert_md_to_Html_with_kikoo(args.input, args.output)
else:
    print('Conversion en cours...')
    convert_md_to_Html(args.input,args.output)
