//load url
PyDoc_STRVAR(webviewLoadURL_doc,
	"load url\n"\
	"\n"\
	"webview.loadURL(url, cleanCache)\n"\
	"\n"\
	"Parameters\n"\
	"----------\n"\
	"    url : string\n"\
	"        the url link to display on webview\n"\
	"    cleanCache : bool\n"\
	"        clean the caching or not. True by default");

//deep link
PyDoc_STRVAR(webviewDeeplink_doc,
    "load the deep link, use internal webview like safari service on ios and ... on android\n"\
    "\n"\
    "webview.deeplink(url)\n"\
    "\n"\
    "Parameters\n"\
    "----------\n"\
    "    url : string\n"\
    "        the url deep link");
