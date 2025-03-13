while True:
    txt = input('\nInsira o link do video original: ').strip()
    
    if "?si=" in txt:
        x = txt.split("be/")
        
        url = x[1]
        url = url.split("?si=")[0]
        
    elif "?v=" in txt:
        x = txt.split("?v=")
        
        url = x[1]
        url = url.split("&")[0]
    
    print('\nLink do video sem anuncios: ')
    print(f'\nwww.youtube-nocookie.com/embed/{url}')
    
    continuar = input('\n\nDeseja continuar? [S/N]').strip().lower()
    
    if continuar != "s":
        break