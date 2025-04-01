MODOS = {
    "claro": {
        "bg": "#f0f0f0",
        "fg": "#000000",
        "button_bg": "#e0e0e0",
        "button_fg": "#000000",
        "text_bg": "#ffffff",
        "text_fg": "#000000",
        "entry_bg": "#ffffff",
        "entry_fg": "#000000",
        "highlight": "#d3d3d3"
    },
    "escuro": {
        "bg": "#2d2d2d",
        "fg": "#ffffff",
        "button_bg": "#3d3d3d",
        "button_fg": "#000000",
        "text_bg": "#1e1e1e",
        "text_fg": "#ffffff",
        "entry_bg": "#3d3d3d",
        "entry_fg": "#ffffff",
        "highlight": "#4d4d4d"
    }
}

def aplicar_modo(janela, widgets, modo):
    cores = MODOS[modo]
    
    janela.configure(bg=cores["bg"])
    
    for widget in widgets:
        widget_type = widget[0]
        widget_obj = widget[1]
        
        if widget_type == "frame":
            widget_obj.config(bg=cores["bg"])
        elif widget_type == "label":
            widget_obj.config(bg=cores["bg"], fg=cores["fg"])
        elif widget_type == "button":
            widget_obj.config(bg=cores["button_bg"], fg=cores["button_fg"],
                            highlightbackground=cores["highlight"])
        elif widget_type == "entry":
            widget_obj.config(bg=cores["entry_bg"], fg=cores["entry_fg"],
                            insertbackground=cores["fg"],
                            highlightbackground=cores["highlight"])
        elif widget_type == "text":
            widget_obj.config(bg=cores["text_bg"], fg=cores["text_fg"],
                            insertbackground=cores["fg"])