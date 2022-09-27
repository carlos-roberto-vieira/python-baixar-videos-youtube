# pip install pytube 
# pip install PySingleGUI 

# pip install pyinstaller
# pyinstaller --onefile -w app.py

from pytube import YouTube
from PySimpleGUI import PySimpleGUI as sg

def download_360p_mp4_videos(url: str, outpath: str = "./"):
    yt = YouTube(url)
    yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(outpath)

if __name__ == "__main__":
    
    #layout PySimpleGUI
    sg.theme('Reddit')
    layout = [
        [ sg.Text( '' )],
        [ sg.Text('Informe a URL do video :')], 
        [ sg.Input( key='url', size=( 50,1) ),  sg.Button( 'Baixar' ) ],
        [ sg.Text( '' )],
        [ sg.Button( 'Sair' )]
    ]
    
    #janela
    janela = sg.Window( 'Baixar VIDEOS do YouTube', layout, size=( 460, 200) )

    while True:
        eventos, valores = janela.read()
        
        if eventos == sg.WIN_CLOSED:
            break
        if eventos == 'Baixar':
            if valores['url'][0:4] == "http":
                download_360p_mp4_videos( valores['url'] )
            else:
                sg.popup( "Informe a url do video", keep_on_top=True )
        if eventos == 'Sair':
            break