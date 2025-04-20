from flask import request
from scan import DocScanner
from views import app_views



@app_views.route('/document',methods=['POST'],strict_slashes=False)
def scan_doc():


    input=request.get_json()
    image_str=input['base64']
    ds=DocScanner()
    image = ds.base64_to_image(base64_str=image_str)
    
       
    if image.any():
        scan=ds.scan(image)
        return scan,200