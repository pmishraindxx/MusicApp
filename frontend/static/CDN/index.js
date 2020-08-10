function uploadsong() {

    submit_btn = document.getElementById('mysubmitbtn');
    
  
    
  
    attachment = document.getElementById('attach');
    title = document.getElementById('title').value;
    artist = document.getElementById('artist').value;
    album = document.getElementById('album').value;
  
    var formData = new FormData();
  
    formData.append('title', title);
    formData.append('artist', artist);
    formData.append('album', album);
  
    for (var i = 0; i < attachment.files.length; i++){
      formData.append('attachment[]', attachment.files[i]);
    }

    $.ajax({
      type: "POST",
      url: "/backend/api_upload_song/",
      data: formData,
      contentType: false,
      processData: false,
      success: function(response){
        submit_btn.style.disable = "disable";
        
      window.open("/", "_self");
      },
      error: function(response) {
         
        window.open("/", "_self");
      }
    });
    }  




    function searchquery() {

        search_term = document.getElementById('search_term').value;
      
        
      
        var formData = new FormData();
      
        formData.append('your_search_query', search_term);

        
        
        $.ajax({
          type: "POST",
          url: "/backend/api_search/",
          data: formData,
          contentType: false,
          processData: false,
          success: function(response){
           
          window.open("/", "_self");
          },
          error: function(response) {
              
            window.open("/", "_self");
          }
        });
        } 
        
        
        function deletesong(song_id) {
          
        
          var formData = new FormData();
        
          formData.append('song_id', song_id);
  
        
          
          $.ajax({
            type: "DELETE",
            url: "/backend/del_song/",
            data: formData,
            contentType: false,
            processData: false,
            success: function(response){
              
            window.open("/", "_self");
            },
            error: function(response) {
                
              window.open("/", "_self");
            }
          });
          }  
    
    
    
    
    
        
      

  