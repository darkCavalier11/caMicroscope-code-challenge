aim : here is the challenge given by caMicroscope org for serving images to the client by
      separate channel and client join them to see full image.

software used: 
1.<nodejs and express> as framework
2.<sharp> package from npm to handlng image channel and servng them.
3.<hbs> a templating engine for rendering and serving client and templating 

workflow: 
here i use a sample image. load it using sharp and then extracting indivisual channel from that 
image and saving it. later serving it to the client with joining the channels.

multiple image handling
fast server node+python
config multer for size and compress image
buffering and asyc
validating image uploads and stoping same image from convertiong multiple time
responsive