from website import create_app

app = create_app()


#we want to run the web server only if this file is running 
if __name__ == '__main__':
    app.run(debug=True) # runs the Flask app and the server
                        # if we make a change to the website, it automatically reruns
    

