from cgi import escape

def main(request, response):
    data = """<!doctype html>
<html>
        <head>
                <title>history.pushState/replaceState and referer headers (before onload)</title>
        </head>
        <body>

                <noscript><p>Enable JavaScript and reload</p></noscript>
                <div id="log"></div>
                <script type="text/javascript">
var httpReferer = "%s";
var lastUrl = location.href.replace(/\/[^\/]*$/,'\/010-4.html?2345');
parent.test(function () {
        parent.assert_equals( httpReferer, lastUrl );
}, 'HTTP Referer should use the replaced state (before onload)');
parent.test(function () {
        parent.assert_equals( document.referrer, lastUrl );
}, 'document.referrer should use the replaced state (before onload)');
parent.done();
                </script>

        </body>
</html>"""

    referrer = request.headers.get("referer", "")

    return [("Content-Type", "text/html")], data % escape(referrer)
