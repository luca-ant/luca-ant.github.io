
jQuery(window).on("load",function(e) {

    // load screen
    jQuery('.loadreveal').addClass('reveal');
    jQuery('#loadscreen').stop().animate( { opacity: 0 }, 200, function() {
        jQuery('body.home').removeClass('loading');
        jQuery(this).hide();
    });


    // masonry gallery
    var $masonry_gallery = jQuery('.masonry-gallery.gallery');
    if ( $masonry_gallery.length > 0 ) {

        $masonry_gallery.each( function(index, element) {
            var $masonry_items = $(element).find('.gallery-item');
        
            // set masonry layout
            $(element).isotope({
                masonry: { columnWidth: $(element).find('.gallery-item')[0] },
                itemSelector: '.gallery-item'
            });
            $(element).isotope('layout');
                
            // filtering
            jQuery('#gallery-filter li a').on('click', function(){
                jQuery('#gallery-filter li a').removeClass('active');
                jQuery(this).addClass('active');
                var selector = jQuery(this).attr('data-filter');
                $masonry_gallery.isotope({ filter: selector });
                return false;
            });

            // changing layout
            jQuery('#grid-changer li a').on('click', function(){
                jQuery('#grid-changer li a').removeClass('active');
                jQuery(this).toggleClass('active');

                $masonry_items.removeClass('col-3');
                $masonry_items.removeClass('col-4');
                $masonry_items.removeClass('col-5');
                $masonry_items.toggleClass(jQuery(this).closest('li').attr('class'));
                $masonry_gallery.isotope('layout');
            });
        
        });
    }

    
    // before-after
    var $before_after = jQuery('.before-after.gallery');
    if ( $before_after.length > 0 ) {
        $before_after.imageReveal({
            barWidth: 4,
            touchBarWidth: 50,
            startPosition: 0.5,
            width: jQuery('.before-after img').width(),
            height:  jQuery('.before-after img').height()
        });
    }

    // changing blog layout
    var $blog_layout = jQuery('#blog-timeline');
    if ( $blog_layout.length > 0 ) {

        jQuery('#grid-changer li a').on('click', function(){
            jQuery('#grid-changer li a').removeClass('active');
            jQuery(this).toggleClass('active');

            $blog_layout.closest('.wrapper').toggleClass('blog-masonry');
            
            if ( $blog_layout.closest('.wrapper').hasClass('blog-masonry') ) {
                jQuery('#blog-post').animate({'left': '100%'}, 400, function() {
                    // set masonry layout
                    $blog_layout.isotope({
                        masonry: { columnWidth: $blog_layout.find('article')[0], gutter: 60 },
                        itemSelector: 'article'
                    });
                    $blog_layout.isotope('layout');
                    jQuery('#blog-post').hide();
                });
            }
            else {
                jQuery('#blog-post').show().animate({'left': '0'}, 400 );
                $blog_layout.isotope('destroy');
                
                if ( $masonry_gallery.length > 0 ) {
                    $masonry_gallery.isotope('layout');
                }
            }
        });
    }
});
