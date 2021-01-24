# -*- coding: utf-8 -*-
from xhtml2pdf import pisa  # import python module

# Define your data
sourceHtml = """<html>
<head>
<style>
    @page {
        size: a4 portrait;
        @frame header_frame {           /* Static Frame */
            -pdf-frame-content: header_content;
            left: 50pt; width: 512pt; top: 50pt; height: 40pt;
        }
        @frame content_frame {          /* Content Frame */
            left: 50pt; width: 512pt; top: 90pt; height: 632pt;
        }
        @frame footer_frame {           /* Another static Frame */
            -pdf-frame-content: footer_content;
            left: 50pt; width: 512pt; top: 772pt; height: 20pt;
        }
    }
</style>
</head>

<body>
    <!-- Content for Static Frame 'header_frame' -->
    <div id="header_content">Lyrics-R-Us</div>

    <!-- Content for Static Frame 'footer_frame' -->
    <div id="footer_content">(c) - page <pdf:pagenumber>
        of <pdf:pagecount>
    </div>

    <!-- HTML Content -->
    To PDF or not to PDF
</body>
</html>"""
outputFilename = "test3.pdf"


# Utility function
def convertHtmlToPdf(sourceHtml, outputFilename):
    # open output file for writing (truncated binary)
    resultFile = open(outputFilename, "w+b")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
        sourceHtml,  # the HTML to convert
        dest=resultFile)  # file handle to recieve result

    # close output file
    resultFile.close()  # close output file

    # return True on success and False on errors
    return pisaStatus.err


# Main program
if __name__ == "__main__":
    pisa.showLogging()
    convertHtmlToPdf(sourceHtml, outputFilename)
