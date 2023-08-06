#pragma once

#ifdef _WIN32
#define IGE_EXPORT __declspec(dllexport)
#else
#define IGE_EXPORT
#endif

class WebViewImpl;
class IGE_EXPORT Webview
{
public:
	Webview();
	~Webview();

    void CreateWebView();
    void RemoveWebView();
	void LoadURL(const char* url, bool cleanCache);
    void Deeplink(const char* url);
	void SetVisible(bool visible);
	void SetRect(int left, int top, int maxWidth, int maxHeight);

	WebViewImpl* GetImpl();

public:
	static WebViewImpl* m_webviewImpl;
};
