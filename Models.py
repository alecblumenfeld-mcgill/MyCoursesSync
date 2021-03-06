import os, os.path


class Course:
    def __init__(self, semster, title, link, element):
        self.semster = semster
        self.title = title
        self.link = link
        self.element = element

    def makeFolder(self):
        if not os.path.exists("testing/" + self.title):
            os.mkdir("testing/" + self.title)



class Document:
    course =""
    def __init__(self, title, link,type, folder,courseTitle):
        self.title = title
        self.link = link
        self.type = type

        self.folder = folder
        self.courseTitle = courseTitle

    def saveFile(self,driver, folder):
        ##check if file exits
        if(os.path.isfile("testing/" +folder.className+"/"+ folder.title+"/"+self.title)):
            #iff it does skip
            pass
        else:
            driver.get(self.link)
            try:
                toDownloadfile = driver.find_element_by_class_name("d2l-fileviewer-pdf")
                link = toDownloadfile.get_attribute("data-location")
                print ("https://mycourses2.mcgill.ca"+link)
            except:
                driver.find_element_by_partial_link_text('Open in New Window').click()
                driver.switch_to_window(driver.window_handles[1])
                link = driver.current_url
                driver.switch_to_window(driver.window_handles[1])
                del driver.window_handles[1]
                print(link)

        pass

    def checkIfFileExists(self):
        path = self.courseTitle+"/"+self.folder


        if not os.path.exists(path):
            os.makedirs(path)
            return False


        path += self.title

        if os.path.exists(path): return True
        else: return False



        pass
    def save(self,agent,path):
        try:
            if self.type == "Link":
                ##TODO: ADD LINK GENERATION
                return ""
            agent.retrieve(self.link,path+self.courseTitle+"/"+self.folder+"/"+self.title+self.type)[0]
            print "Downloaded "+ self.title
        except:
            print "unable to download file "+ self.title
            pass
    pass

		




