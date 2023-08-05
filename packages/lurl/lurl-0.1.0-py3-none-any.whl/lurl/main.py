from optparse import OptionParser
import sys
from . import tkp_struct, args_parser, multihar
from collections import OrderedDict

def main():
    parser, options, arguments = args_parser.parse_options()
    
    if not options.curl_prod is None or not options.curl_stag is None:
        req = tkp_struct.TkpStruct(options.curl_prod,options.curl_stag)
        req.get_as_tkp()

    if not options.stag_har_folder is None or not options.prod_har_folder is None :
        curls_stag = curls_prod = curls_presenter = OrderedDict()
        if not options.stag_har_folder is None :
            curls_stag = multihar.get_curls(options.stag_har_folder)
            curls_presenter = curls_stag
        if not options.prod_har_folder is None:
            curls_prod = multihar.get_curls(options.prod_har_folder)
            curls_presenter = curls_prod
        for file_id, curl in curls_presenter.items(): 
            curl_prod = curls_prod[file_id] if file_id in curls_prod else None
            curl_stag = curls_stag[file_id] if file_id in curls_stag else None
            req = tkp_struct.TkpStruct(curl_prod=curl_prod, curl_stag=curl_stag, file_id=file_id)
            req.get_as_tkp()
    
    sys.exit(0)

if __name__ == '__main__':
    main()