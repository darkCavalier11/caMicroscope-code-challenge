aim : here is the challenge given by caMicroscope org for serving images to the client by
      separate channel and client join them to see full image.

software used: 
1.<nodejs/express> as framework
2.<hbs> a templating engine for rendering and serving client and templating 
3.<opencv-python> for image handling, manpla

initialising: 
please command 'npm start' to start the server at PORT 3000.

workflow:
a web page served at port 3000. pls attach a valid image file and click on channel. the image file saved by sever in a directory at ./views/uploads.
when channel button is clicked image from uploads directory turned into individual channels by a python file named imageChanneler.py.
it uses opencv-python which called by node programme itself for the conversion.
when clicked on merge a separate webpage pops which show individual merges of all channels:


why?
python is widely used for cv and for future development python environment is more suitable.
also when handling multiple routes it is good to shift its loads to other side application so that server can be free at that particular time for
other requests. Not Django but node due to its scalability with express and with rich library support and on top of that high performance of node
over django.

current issues:
buffering and async handling of image uploads
validating image uploads and stoping same image from convertiong multiple time
responsive website
testing the performance of server.