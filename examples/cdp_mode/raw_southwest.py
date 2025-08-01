from seleniumbase import SB

with SB(uc=True, test=True, locale="en", ad_block=True) as sb:
    url = "https://www.southwest.com/air/booking/"
    sb.activate_cdp_mode(url)
    sb.sleep(2.8)
    origin = "BOS"
    destination = "MDW"
    sb.cdp.click_if_visible("button#onetrust-accept-btn-handler")
    sb.sleep(0.5)
    sb.cdp.gui_click_element("input#originationAirportCode")
    sb.sleep(0.2)
    sb.cdp.select("input#originationAirportCode").clear_input()
    sb.sleep(0.2)
    sb.uc_gui_press_keys(" " + "\n")
    sb.sleep(0.5)
    sb.cdp.gui_click_element("input#originationAirportCode")
    sb.sleep(0.4)
    sb.uc_gui_press_keys(origin + "\n")
    sb.sleep(0.4)
    sb.cdp.gui_click_element("h1")
    sb.sleep(0.3)
    sb.cdp.gui_click_element("input#destinationAirportCode")
    sb.sleep(0.2)
    sb.cdp.select("input#destinationAirportCode").clear_input()
    sb.sleep(0.2)
    sb.uc_gui_press_keys(destination + "\n")
    sb.sleep(0.4)
    sb.cdp.gui_click_element("h1")
    sb.sleep(0.2)
    sb.cdp.click_if_visible("button#onetrust-accept-btn-handler")
    sb.sleep(0.1)
    sb.cdp.click('form button[data-test="submitField"]')
    sb.sleep(2.5)
    sb.cdp.click('button[aria-labelledby*="nearby-airport-drawer-"]')
    sb.sleep(4)
    day = sb.cdp.get_text('[aria-current="true"] span[class*="cal"]')
    print("**** Flights from %s to %s ****" % (origin, destination))
    flights = sb.find_elements("li.air-booking-select-detail")
    for flight in flights:
        info = flight.text
        departs = info.split("Departs")[-1].split("M")[0].strip() + "M"
        arrives = info.split("Arrives")[-1].split("M")[0].strip() + "M"
        stops = flight.query_selector(".flight-stops-badge").text
        duration = flight.query_selector('[class*="flight-duration"]').text
        p_elm = flight.query_selector('span.currency span[aria-hidden]')
        if not p_elm:
            continue
        price = p_elm.text
        print(f"* {day}, {departs} -> {arrives} ({stops}: {duration}) {price}")
