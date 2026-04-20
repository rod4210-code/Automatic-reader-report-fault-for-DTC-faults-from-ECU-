import html

class HTML_Look_Faults:
    def __init__(self, html_content):
        self.html_content = html_content

    def extract_fault_status(self):
        # Parse the HTML content
        parsed_html = html.fromstring(self.html_content)
        
        # Extract FaultStatus hex values
        fault_statuses = parsed_html.xpath('//FaultStatus/text()')  # Adjust the XPath as necessary
        hex_values = [status for status in fault_statuses]
        return hex_values
