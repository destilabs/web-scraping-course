def get_element_by_selector(html, selector):
    elem = html.find_elements_by_css_selector(selector)

    if len(elem) > 0:
        return next(iter(elem)).text.replace('\n',' ').strip()
    else: 
        print(f'Missing value for selector {selector}')
        return ''