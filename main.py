from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) 
    #Turn off Debugging when deploying to Cloud RUN, using it during developing time, to keep refresing the HTTP server as I do changes to the code