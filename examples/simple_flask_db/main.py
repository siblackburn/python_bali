from application import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')

##telling the app to run on this ip address. 0.0.0.0 means run it on all network interfaces
#main method gets called first, and then that runs the app