'''
<div class="row">
        <div class="title text-center">
          <h2>Trendy Products</h2>
        </div>
      </div>
   
       
        {% for dev in home %}

          <div id="" class="col-lg-3 col-sm-6 col-md-5 devkh dev{{dev.categor.id}}">
               <img  class="thumbnail" src="{{dev.photo.url}}">
               <div class="box-element product">
                    <h6><strong>{{dev.name}}</strong></h6>
                    <h4 style="display: inline-block; float: right"><strong>${{dev.price|floatformat:2}}</strong></h4>
                    <br>
                    <hr>
          
                    <button  class="btn btn-outline-secondary add-btn">Add to Cart</button>
                    <a class="btn btn-outline-success" href="#">View</a>
          
               </div>
          </div>
          
          {% endfor %}
     
       </div>
       '''