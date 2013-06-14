# Create your views here.
#from IconWrite.IconWriteApp.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from gstudio.forms import ImageForm
from gstudio.methods import *


from demo.settings import *
from gstudio.models import *
from objectapp.models import *
import os
from gstudio.methods import *
from PIL import Image
import glob, os
import hashlib
from django.template.defaultfilters import slugify
from django.template.loader import get_template
from django.template import Context


size = 128, 128
report = "true"
md5_checksum = ""




def Interface(request):
	p1=Objecttype.objects.get(title="Image")
	q1=p1.get_nbh['contains_members']
	subjectimage = q1.filter(tags__icontains="Subject")
	verbimage = q1.filter(tags__icontains="Verb")
	objectimage=q1.filter(tags__icontains="Object")
	delete = request.POST.get("delete","")
	pict = request.POST.get("pict","")
	



	if delete != "":
			each=q1.get(id=pict)
			each.delete()
			ti=each.title
			os.system("rm -f "+MEDIA_ROOTNEW+'/'+ti)
			p1=Objecttype.objects.get(title="Image")
			q1=p1.get_nbh['contains_members']
			subjectimage = q1.filter(tags__icontains="Subject")
			
			return render_to_response('metadashboard/interface_iconwrite.html',
				context_instance=RequestContext(request,{"subjectimage":subjectimage,"verbimage":verbimage,"objectimage":objectimage})
				 )

	'''
	if p1 != ""    :			
		        title= q1.get(id=titl)
			titleid=request.GET['titleid']
			p1=Objecttype.objects.get(title="Image")
			q1=p1.get_nbh['contains_members']
			q1.title=title
			q1.save()
			
			p1=Objecttype.objects.get(title="Image")
			q1=p1.get_nbh['contains_members']
			subjectimage = q1.filter(tags__icontains="Subject")
			
			return render_to_response('metadashboard/interface_iconwrite.html',
				context_instance=RequestContext(request,{"subjectimage":subjectimage,"verbimage":verbimage,"objectimage":objectimage})
				 )

	'''

	
	return render_to_response('metadashboard/interface_iconwrite.html',
				context_instance=RequestContext(request,{"subjectimage":subjectimage,"verbimage":verbimage,"objectimage":objectimage})
				 )



def Subject(request):

	p1=Objecttype.objects.get(title="Image")
	q1=p1.get_nbh['contains_members']
	
        category=""

	# Upload scenario	
	if request.method=="POST":
		
		title = request.POST.get("title1","")
		category = request.POST.get("choose","")

		
		user = request.POST.get("user","")
		delete = request.POST.get("delete","")
		
		imgid = request.POST.get("imgid","")
		pict = request.POST.get("pict","")
		fulid = request.POST.get("fulid","")
		show_sub = request.POST.get("Show","")	
			
		
	
	a=[]
	reportid=''

	
	if category :
		for each in request.FILES.getlist("image[]",""):
			a.append(each)
			if a != "":
				i=0
				for f in a:
					if i==0:
						if category == "Subject":
							report,imageeachid = save_subimage(f,title,user)
							if report == "false":
								reportid = imageeachid
							else:
								create_object_sub(f,user,title,str(request.user),category)
								i=i+1
						
						if category == "Verb":
							report,imageeachid = save_verimage(f,title,user)
							if report == "false":
								reportid = imageeachid
							else:
								create_object_sub(f,user,title,str(request.user),category)
								i=i+1	


						if category == "Object":
							report,imageeachid = save_objimage(f,title,user)
							if report == "false":
								reportid = imageeachid
							else:
								create_object_sub(f,user,title,str(request.user),category)
								i=i+1						
				

					else:	
						report,imageeachid = save_subimage(f,title+'_'+str(i),user)
						if report == "false":
							reportid = imageeachid
						else:
							create_object_sub(f,user,title+'_'+str(i),str(request.user),category)
							i=i+1
	print "after for"
	p1=Objecttype.objects.get(title="Image")
	q1=p1.get_nbh['contains_members']
			
	return HttpResponseRedirect("/iconwrite/")





def save_subimage(file,title, user, path=""):
	print "inside Subject save file"
        report = "true"
	imageeachid = ''
	filename = title
	slugfile = str(file)
	slugfile=slugfile.replace(' ','_')
	os.system("mkdir -p "+ MEDIA_ROOTNEW4+"/"+user)
    	fd = open('%s/%s/%s' % (MEDIA_ROOTNEW4, str(user),str(path) + str(slugfile)), 'wb')

    	for chunk in file.chunks():
        	fd.write(chunk)
    		fd.close()

	global md5_checksum1
	md5_checksum1 = md5Checksum_sub(MEDIA_ROOTNEW4+"/"+ str(user)+"/"+slugfile)
	attype = Attributetype.objects.get(title="md5_checksum_image")
	att = Attribute.objects.all()
	
	flag = 0
	for each in att:
		if each.attributetype.id == attype.id:
			if each.svalue == md5_checksum :
				flag = 1
				imageeachid = each.subject.id
	if flag == 1:
		report = "false"
	else:	
		for infile in glob.glob(MEDIA_ROOTNEW4+"/"+str(user)+"/"+str(slugfile)):
			file, ext = os.path.splitext(infile)
			im = Image.open(infile)
			imm = Image.open(infile)
			im.thumbnail(size, Image.ANTIALIAS)
			im.save(file + "-thumbnail", "JPEG")
			width, height = imm.size
			sizem = 1024,height
			if int(width) > 1024:
				imm.thumbnail(sizem, Image.ANTIALIAS)
				imm.save(file + "_display_1024","JPEG")
			else:
				imm.thumbnail(imm.size,Image.ANTIALIAS)
				imm.save(file + "_display_1024","JPEG")
    	return report,imageeachid	


def save_verimage(file,title, user, path=""):
	print "inside Subject save file"
        report = "true"
	imageeachid = ''
	filename = title
	slugfile = str(file)
	slugfile=slugfile.replace(' ','_')
	os.system("mkdir -p "+ MEDIA_ROOTNEW5+"/"+user)
    	fd = open('%s/%s/%s' % (MEDIA_ROOTNEW5, str(user),str(path) + str(slugfile)), 'wb')
	   	
	for chunk in file.chunks():
        	fd.write(chunk)
    		fd.close()

	global md5_checksum1
	md5_checksum1 = md5Checksum_sub(MEDIA_ROOTNEW5+"/"+ str(user)+"/"+slugfile)
	attype = Attributetype.objects.get(title="md5_checksum_image")
	att = Attribute.objects.all()
	
	for each in att:
		if each.attributetype.id == attype.id:
			if each.svalue == md5_checksum1 :
				
				imageeachid = each.subject.id
	
    	return report,imageeachid





def save_objimage(file,title, user, path=""):
	print "inside Subject save file"
        report = "true"
	imageeachid = ''
	filename = title
	slugfile = str(file)
	slugfile=slugfile.replace(' ','_')
	os.system("mkdir -p "+ MEDIA_ROOTNEW6+"/"+user)
    	fd = open('%s/%s/%s' % (MEDIA_ROOTNEW6, str(user),str(path) + str(slugfile)), 'wb')

    	for chunk in file.chunks():
        	fd.write(chunk)
    		fd.close()

	global md5_checksum1
	md5_checksum1 = md5Checksum_sub(MEDIA_ROOTNEW6+"/"+ str(user)+"/"+slugfile)
	attype = Attributetype.objects.get(title="md5_checksum_image")
	att = Attribute.objects.all()
	
	for each in att:
		if each.attributetype.id == attype.id:
			if each.svalue == md5_checksum1 :

				imageeachid = each.subject.id			
	
    	return report,imageeachid




def md5Checksum_sub(filePath):
    fh = open(filePath, 'rb')
    m = hashlib.md5()
    while True:
        data = fh.read(8192)
        if not data:
            break
        m.update(data)
    return m.hexdigest()



def create_object_sub(f,log,title,usr,category):
	
	print "inside Subject create object"
	p1=Gbobject()

	filename = str(f)
	filename=filename.replace(' ','_')
	p1.title=title
	
        fname=slugify(title)+"-"+usr
	p1.image=log+"/"+filename
	
	p1.slug=slugify(p1.title)
	
	p1.status=2
        p1.tags = category
	p1.save()
	p1.slug = p1.slug + "-" + str(p1.id)
	p1.sites.add(Site.objects.get_current())
	p1.save()
	s=Author.objects.get(username=log)
	p1.authors.add(s)
	p1.save()
	q1=Objecttype.objects.get(title="Image")
	p1.objecttypes.add(Objecttype.objects.get(id=q1.id))    
	p1.save()
	
 	ext='.org'
        html='.html'
 	myfile = open(os.path.join(FILE_URL,fname+ext),'w')
	
	myfile.close()
	myfile = open(os.path.join(FILE_URL,fname+ext),'r')
        rfile=myfile.readlines()
	scontent="".join(rfile)
	newcontent=scontent.replace("\r","")
	myfile = open(os.path.join(FILE_URL,fname+ext),'w') 
	myfile.write(newcontent)
	#myfile.readline()
	myfile = open(os.path.join(FILE_URL,fname+ext),'a')
	myfile.write("\n#+OPTIONS: timestamp:nil author:nil creator:nil  H:3 num:nil toc:nil @:t ::t |:t ^:t -:t f:t *:t <:t")
	myfile.write("\n#+TITLE: ")
	myfile = open(os.path.join(FILE_URL,fname+ext),'r')
	stdout = os.popen("%s %s %s"%(PYSCRIPT_URL_GSTUDIO,fname+ext,FILE_URL))
	output = stdout.read()
	data = open(os.path.join(FILE_URL,fname+html))
 	data1 = data.readlines()
 	data2 = data1[68:]
       # dataa = data2[data2.index('<div id="content">\n')]='<div id=" "\n'

 	data3 = data2[:-2]
 	newdata=""
 	for line in data3:
        	newdata += line.lstrip()
 	
 	p1.save()
        a=Attribute()
        a.attributetype=Attributetype.objects.get(title="md5_checksum_image")
        a.subject=p1
        a.svalue=md5_checksum1
        a.save()
'''
def edit_title(request):
	nidtitle = ""
	if request.method =="GET":
		print "iin get "
		title=request.GET['title']
		titleid=request.GET['titleid']
		nid=NID.objects.get(id=titleid)
		nid.title=title
		nid.save()
		nid=NID.objects.get(id=titleid)
		nidtitle = nid.title
  	t = get_template('gstudio/editedobjecttitle.html')
	html = t.render(Context({'title':nidtitle}))
	return HttpResponse(html)

'''





