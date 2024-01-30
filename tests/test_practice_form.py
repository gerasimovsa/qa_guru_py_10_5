import time

from selene import browser, be, have, by, command


def test_submit_form():
    browser.open("/automation-practice-form")
    browser.element("#firstName").should(be.blank).type("Stefan")
    browser.element("#lastName").should(be.blank).type("Burnett")
    browser.element("#userEmail").should(be.blank).type("mcride_dg@gmail.com")
    browser.element("label[for='gender-radio-1']").click()
    browser.element("#userNumber").should(be.blank).type("7148088000")
    browser.element("#dateOfBirthInput").click()
    browser.element("[class='react-datepicker__year-select']").click()
    browser.element(by.text("1978")).click()
    browser.element("[class='react-datepicker__month-select']").click()
    browser.element(by.text("May")).click()
    browser.element("[class='react-datepicker__year-select']").click()
    browser.element("[class = 'react-datepicker__day react-datepicker__day--010']").click()
    browser.element("#subjectsInput").should(be.blank).type("Chemistry")
    browser.element("#react-select-2-option-0").click()
    browser.element("label[for='hobbies-checkbox-3']").click()
    browser.element("#uploadPicture").send_keys(__file__.replace('tests\\test_practice_form.py', 'data\\mc_ride.png'))
    browser.element("#currentAddress").should(be.blank).type("888 East Las Olas Blvd, Suite 710")
    browser.element("#submit").perform(command.js.scroll_into_view)
    browser.element("#state").click()
    browser.element(by.text("NCR")).click()
    browser.element("#city").click()
    browser.element("div[id='react-select-4-option-0']").click()
    browser.element("#submit").click()

    browser.element(".table").should(be.present)
    browser.all('tr td:first-child + td').should(have.exact_texts(
        "Stefan Burnett",
        "mcride_dg@gmail.com",
        "Male",
        "7148088000",
        "10 May,1978",
        "Chemistry",
        "Music",
        "mc_ride.png",
        "888 East Las Olas Blvd, Suite 710",
        "NCR Delhi"))

    browser.element("#closeLargeModal").click()
    browser.element(".table").should(be.not_.present)
