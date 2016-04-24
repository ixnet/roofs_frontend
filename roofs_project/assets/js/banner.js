jQuery(function($) {

      
      $('#background-video').YTPlayer({
        fitToBackground: true,
        videoId: '4EoUz39nPMM',
        pauseOnScroll: true,
        callback: function() {
          videoCallbackEvents();
        }
      });
      
      var videoCallbackEvents = function() {
        var player = $('#background-video').data('ytPlayer').player;
      
        player.addEventListener('onStateChange', function(event){
            console.log("Player State Change", event);

            // OnStateChange Data
            if (event.data === 0) {          
                console.log('video ended');
            }
            else if (event.data === 2) {          
              console.log('paused');
            }
        });
      }
    });