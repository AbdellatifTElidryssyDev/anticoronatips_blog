var arrLang = new Array();
    arrLang['en'] = new Array();
    arrLang['km'] = new Array();

    // English content
    arrLang['en']['home'] = 'Home';
    arrLang['en']['about'] = 'About Us';
    arrLang['en']['contact'] = 'Contact Us';
    arrLang['en']['desc'] = 'This is my description';

    // Khmer content (Cambodian Language) 
    // Please change to your own language
    arrLang['ar']['home'] = 'الرئسية';
    arrLang['ar']['about'] = 'احاديث دينية';
    arrLang['ar']['contact'] = 'فيديوهات';
    arrLang['ar']['desc'] = 'كورونا حول العالم';

    // Process translation
    $(function() {
      $('.translate').click(function() {
        var lang = $(this).attr('id');

        $('.lang').each(function(hadiths, item) {
          $(this).text(arrLang[lang][$(this).attr('key')]);
        });
      });
    });
