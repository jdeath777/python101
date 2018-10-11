#To extract phone number from a string

import re
#declare  a variable to store the string
str = '''<a aria-label="Spokeo Logo" class="header-logo block" href="/"></a
         <a class="floating-link" href="/about" rel="nofollow">ABOUT</a>,
          <a class="floating-link" href="/login?url=/425-205" rel="nofollow">LOGIN</a>,
           <a class="floating-link promoted" href="/purchase?url=/425-205" rel="nofollow">Sign Up</a>,
            <a aria-label="Spokeo Logo" class="header-menu-logo header-logo" href="/"></a>,
             <a class="header-menu-item display-3 truncate" href="/purchase?url=/425-205"><i class="v10-icon v10-icon-user-plus right-m-lg text-blue xs"></i><span>Sign Up</span></a>,
              <a class="header-menu-item display-3 truncate" href="/login?url=/425-205"><i class="v10-icon v10-icon-login right-m-lg text-blue xs"></i><span>Login</span></a>,
               <a class="header-menu-item display-3 truncate" href="https://help.spokeo.com"><i class="v10-icon v10-icon-help-circled right-m-lg text-blue xs"></i><span>Get Help</span></a>,
                <a href="/about">About</a>,
                 <a href="/careers">Careers</a>,
                  <a href="/compass">Blog</a>,
                   <a href="/privacy">Privacy</a>,
                    <a href="/terms-of-use-consumer">Terms</a>,
                     <a href="/contact">Contact</a>,
                      <a class="sub_panel_nav_item js_smooth_scroll icon_jewel_block " href="#profile_summary">(425) 205 in <span {}="">Bothell</span>, <span []="">WA</span>
                       <i class="icon-right-open"></i>
                        </a>,
                         <a class="sub_panel_nav_item js_smooth_scroll icon_jewel_block " href="#phone_numbers">425-205 numbers<span class="sub_panel_nav_count">(8)</span>
                          <i class="icon-right-open"></i>
                           </a>,
                            <a class="sub_panel_nav_item js_smooth_scroll icon_jewel_block " href="#phone_stats">Average Phone Statistics for 425-205
                             <i class="icon-right-open"></i>
                              </a>,
                               <a class="sub_panel_nav_item js_smooth_scroll icon_jewel_block " href="#facts-and-stats">NEIGHBORHOOD STATISTICS
                                <i class="icon-right-open"></i>
                                 </a>,
                                  <a class="breadcrumb_link" href="/WA-area-code" ng_href="/WA-area-code{{vm.MapExpansion.expandMapLink()}}">
                                   <span>
                                    WA area codes
                                     </span>
                                      </a>,
                                       <a class="breadcrumb_link" href="/425-area-code" ng_href="/425-area-code{{vm.MapExpansion.expandMapLink()}}">
                                        <span>
                                         425
                                          </span>
                                           </a>,
                                            <a class="breadcrumb_link" href="/425-205" ng_href="/425-205{{vm.MapExpansion.expandMapLink()}}">
                                             <span>
                                              425-205
                                               </span>
                                                </a>,
                                                 <a class="listview_primary_title" href="/425-205-0017"><span itemprop="telephone">(425) 205-0017</span></a>,
                                                  <a href="/425-205-0017" itemprop="url">Halbert D******</a>,
                                                   <a href="/425-205-0017" itemprop="url">Drkblubathwa L******</a>,
                                                    <a class="button md_button green_button border_button block_button" href="/425-205-0017" itemprop="url">SEE RESULTS</a>,
                                                     <a class="listview_primary_title" href="/425-205-0056"><span itemprop="telephone">(425) 205-0056</span></a>,
                                                      <a href="/425-205-0056" itemprop="url">Jennifer C******</a>,
                                                       <a href="/425-205-0056" itemprop="url">Jennifer C******</a>,
                                                        <a class="button md_button green_button border_button block_button" href="/425-205-0056" itemprop="url">SEE RESULTS</a>,
                                                         <a class="listview_primary_title" href="/425-205-0006"><span itemprop="telephone">(425) 205-0006</span></a>,
                                                          <a href="/425-205-0006" itemprop="url">Hotmail R******</a>,
 <a class="button md_button green_button border_button block_button" href="/425-205-0006" itemprop="url">SEE RESULTS</a>,
  <a class="listview_primary_title" href="/425-205-0062"><span itemprop="telephone">(425) 205-0062</span></a>,
   <a href="/425-205-0062" itemprop="url">Lincoln P******</a>,
    <a class="button md_button green_button border_button block_button" href="/425-205-0062" itemprop="url">SEE RESULTS</a>,
     <a class="listview_primary_title" href="/425-205-0099"><span itemprop="telephone">(425) 205-0099</span></a>,
      <a href="/425-205-0099" itemprop="url">Mary B******</a>,
       <a class="button md_button green_button border_button block_button" href="/425-205-0099" itemprop="url">SEE RESULTS</a>,
        <a class="listview_primary_title" href="/425-205-0060"><span itemprop="telephone">(425) 205-0060</span></a>,
         <a href="/425-205-0060" itemprop="url">Corcoran G******</a>,
          <a class="button md_button green_button border_button block_button" href="/425-205-0060" itemprop="url">SEE RESULTS</a>,
           <a class="pagination_item disabled">PREVIOUS</a>,
            <a class="pagination_item text_jewel blue_jewel border_jewel">1</a>,
             <a class="pagination_item" href="#phone_numbers">2</a>,
              <a class="pagination_item" href="#phone_numbers">NEXT</a>,
               <a href="/about">About</a>,
                <a href="/terms-of-use">Terms</a>,
                 <a href="/privacy">Privacy</a>,
                  <a href="/contact">Contact</a>,
                   <a href="/careers">Careers</a>,
                    <a href="https://help.spokeo.com">Help</a>,
                     <a href="/compass">Blog</a>,
                      <a href="http://www.spokeoaffiliates.com">Affiliates</a>,
                       <a href="/">People Search</a>,
                        <a href="/email-search">Email Lookup</a>,
                         <a href="/directory">People Directory</a>,
                          <a href="/reverse-address-search">Address Search</a>,
                           <a href="/reverse-phone-lookup">Phone Lookup</a>,
                            <a aria-label="Spokeo Twitter Channel" href="https://twitter.com/spokeo" rel="noopener" target="_blank"><i class="v10-icon v10-icon-twitter social xs"></i></a>,
                             <a aria-label="Spokeo Youtube Channel" href="https://www.youtube.com/user/spokeo" rel="noopener" target="_blank"><i class="v10-icon v10-icon-youtube social xs"></i></a>,
                              <a aria-label="Spokeo Facebook Channel" href="https://www.facebook.com/Spokeo" rel="noopener" target="_blank"><i class="v10-icon v10-icon-facebook social xs"></i></a>,
                               <a aria-label="Spokeo Linkedin Channel" href="https://www.linkedin.com/company/spokeo" rel="noopener" target="_blank"><i class="v10-icon v10-icon-linkedin social xs"></i></a>'''

print("The list of phone numbers present in the file are :")

#use the re.findall with the pattern to match the phone number


for i in re.findall(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b',str):
    print(i)

