#!/usr/bin/python
import os
import sys
import getopt
import yaml
import datetime

def main(argv):
    title = ''
    now = datetime.datetime.now()
    date_short = now.strftime("%Y-%m-%d")
    date_long = now.strftime("%Y-%m-%d %H:%M:%S")

    try:
        opts, args = getopt.getopt(argv,"ht:",["help=","title="])
    except getopt.GetoptError:
        print 'blog.py -t <title>'
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print 'blog.py -t <title>'
            sys.exit(2)
        elif opt in ("-t", "--title"):
            title = arg
        else:
            sys.exit(2)

    slug = slugize(date_short,title)
    template = { "date": date_long, "layout": "post", "slug": slug, "status": "draft", "title": title}

    loc = os.path.dirname(os.path.realpath(__file__))

    f = file(loc+'/../_posts/'+slug+'.md', 'w')
    f.writelines("---\n")
    for k,v in template.items():
        f.writelines("{}: {}\n".format(k,v))
    f.writelines("---\n")

    f.close

def slugize(date_short, title):
    return "{}-{}".format(str(date_short),str(title).lower().replace(" ", "-").replace(",",""))

if __name__ == "__main__":
    main(sys.argv[1:])