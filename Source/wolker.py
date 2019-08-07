#Скрытый функционал

'''driver.get_screenshot_as_file('/home/frizik/test.png') 
driver.save_screenshot('/home/frizik/test.png')'''
   

'''upload = vk_api.VkUpload(vk_session)
    photo = upload.photo('/home/frizik/Photo/москва/DSC05281.JPG',album_id=264629427,group_id=184430889)
    vk_photo_url = 'https://vk.com/photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id'])
    print(photo, '\nLink: ', vk_photo_url)
    WriteMsgFunc(event.user_id,photo_url,random_id,vk)'''