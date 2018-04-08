# Copyright (C) 2018 Pohoda-mserver-client authors. See the AUTHORS file found
# in the top-level directory of this distribution.
#
# Licensed under the MIT (Expat) License. See the LICENSE file found in the
# top-level directory of this distribution.

import pohoda_mserver_client.schema.xsd


URI = 'http://www.stormware.cz/schema/version_2/type.xsd'


def dump_ico_type(name, ico):
    if len(ico) > 15:
        raise ValueError()

    return pohoda_mserver_client.schema.xsd.dump_string(name, ico)


def load_accounting_type(accounting_type_dump):
    id_ = None
    id_dump = accounting_type_dump.find(f'{{{URI}}}id')
    if id_dump is not None:
        id_ = load_id_type(id_dump)

    ids = None
    ids_dump = accounting_type_dump.find(f'{{{URI}}}ids')
    if ids_dump is not None:
        ids = load_ids_type(ids_dump)

    type_ = None
    type_dump = accounting_type_dump.find(f'{{{URI}}}accountingType')
    if type_dump is not None:
        type_ = pohoda_mserver_client.schema.xsd.load_string(type_dump)

    return AccountingType(id_, ids, type_)


def load_address(address_dump):
    if address_dump.find(f'{{{URI}}}extId') is not None:
        raise ValueError
    if address_dump.find(f'{{{URI}}}shipToAddress') is not None:
        raise ValueError

    id_ = None
    id_dump = address_dump.find(f'{{{URI}}}id')
    if id_dump is not None:
        id_ = load_id_type(id_dump)

    address = None
    address_dump = address_dump.find(f'{{{URI}}}address')
    if address_dump is not None:
        address = load_address_type(address_dump)

    return Address(id_, address)


def load_address_internet_type(address_internet_type_dump):
    company = None
    company_dump = address_internet_type_dump.find(f'{{{URI}}}company')
    if company_dump is not None:
        company = load_string_company(company_dump)

    title = None
    title_dump = address_internet_type_dump.find(f'{{{URI}}}title')
    if title_dump is not None:
        title = load_string7(title_dump)

    surname = None
    surname_dump = address_internet_type_dump.find(f'{{{URI}}}surname')
    if surname_dump is not None:
        surname = load_string32(surname_dump)

    name = None
    name_dump = address_internet_type_dump.find(f'{{{URI}}}name')
    if name_dump is not None:
        name = load_string32(name_dump)

    city = None
    city_dump = address_internet_type_dump.find(f'{{{URI}}}city')
    if city_dump is not None:
        city = load_string45(city_dump)

    street = None
    street_dump = address_internet_type_dump.find(f'{{{URI}}}street')
    if street_dump is not None:
        street = load_string64(street_dump)

    number = None
    number_dump = address_internet_type_dump.find(f'{{{URI}}}number')
    if number_dump is not None:
        number = load_string10(number_dump)

    zip_ = None
    zip_dump = address_internet_type_dump.find(f'{{{URI}}}zip')
    if zip_dump is not None:
        zip_ = load_string15(zip_dump)

    ico = None
    ico_dump = address_internet_type_dump.find(f'{{{URI}}}ico')
    if ico_dump is not None:
        ico = load_ico_type(ico_dump)

    dic = None
    dic_dump = address_internet_type_dump.find(f'{{{URI}}}dic')
    if dic_dump is not None:
        dic = load_dic_type(dic_dump)

    ic_dph = None
    ic_dph_dump = address_internet_type_dump.find(f'{{{URI}}}icDph')
    if ic_dph_dump is not None:
        ic_dph = load_ic_dph_type(ic_dph_dump)

    phone = None
    phone_dump = address_internet_type_dump.find(f'{{{URI}}}phone')
    if phone_dump is not None:
        phone = load_string40(phone_dump)

    mobil_phone = None
    mobil_phone_dump = address_internet_type_dump.find(f'{{{URI}}}mobilPhone')
    if mobil_phone_dump is not None:
        mobil_phone = load_string24(mobil_phone_dump)

    fax = None
    fax_dump = address_internet_type_dump.find(f'{{{URI}}}fax')
    if fax_dump is not None:
        fax = load_string24(fax_dump)

    email = None
    email_dump = address_internet_type_dump.find(f'{{{URI}}}email')
    if email_dump is not None:
        email = load_string98(email_dump)

    www = None
    www_dump = address_internet_type_dump.find(f'{{{URI}}}www')
    if www_dump is not None:
        www = load_string32(www_dump)

    return AddressInternetType(company, title, surname, name, city, street, number, zip_, ico, dic, ic_dph, phone, mobil_phone, fax, email, www)


def load_address_type(address_type_dump):
    company = None
    company_dump = address_type_dump.find(f'{{{URI}}}company')
    if company_dump is not None:
        company = load_string_company(company_dump)

    division = None
    division_dump = address_type_dump.find(f'{{{URI}}}division')
    if division_dump is not None:
        division = load_string32(division_dump)

    name = None
    name_dump = address_type_dump.find(f'{{{URI}}}name')
    if name_dump is not None:
        name = load_string32(name_dump)

    city = None
    city_dump = address_type_dump.find(f'{{{URI}}}city')
    if city_dump is not None:
        city = load_string45(city_dump)

    street = None
    street_dump = address_type_dump.find(f'{{{URI}}}street')
    if street_dump is not None:
        street = load_string64(street_dump)

    zip_ = None
    zip_dump = address_type_dump.find(f'{{{URI}}}zip')
    if zip_dump is not None:
        zip_ = load_string15(zip_dump)

    ico = None
    ico_dump = address_type_dump.find(f'{{{URI}}}ico')
    if ico_dump is not None:
        ico = load_ico_type(ico_dump)

    dic = None
    dic_dump = address_type_dump.find(f'{{{URI}}}dic')
    if dic_dump is not None:
        dic = load_dic_type(dic_dump)

    vat_payer_type = None
    vat_payer_type_dump = address_type_dump.find(f'{{{URI}}}VATPayerType')
    if vat_payer_type_dump is not None:
        vat_payer_type = load_vat_payer_type_type(vat_payer_type_dump)

    ic_dph = None
    ic_dph_dump = address_type_dump.find(f'{{{URI}}}icDph')
    if ic_dph_dump is not None:
        ic_dph = load_ic_dph_type(ic_dph_dump)

    country = None
    country_dump = address_type_dump.find(f'{{{URI}}}country')
    if country_dump is not None:
        country = load_ref_type(country_dump)

    phone = None
    phone_dump = address_type_dump.find(f'{{{URI}}}phone')
    if phone_dump is not None:
        phone = load_string40(phone_dump)

    mobil_phone = None
    mobil_phone_dump = address_type_dump.find(f'{{{URI}}}mobilPhone')
    if mobil_phone_dump is not None:
        mobil_phone = load_string24(mobil_phone_dump)

    fax = None
    fax_dump = address_type_dump.find(f'{{{URI}}}fax')
    if fax_dump is not None:
        fax = load_string24(fax_dump)

    email = None
    email_dump = address_type_dump.find(f'{{{URI}}}email')
    if email_dump is not None:
        email = load_string98(email_dump)

    return AddressType(company, division, name, city, street, zip_, ico, dic, vat_payer_type, ic_dph, country, phone, mobil_phone, fax, email)


def load_boolean(boolean_dump):
    return pohoda_mserver_client.schema.xsd.load_string(boolean_dump)


def load_classification_vat_type(classification_vat_type_dump):
    id_ = None
    id_dump = classification_vat_type_dump.find(f'{{{URI}}}id')
    if id_dump is not None:
        id_ = load_id_type(id_dump)

    ids = None
    ids_dump = classification_vat_type_dump.find(f'{{{URI}}}ids')
    if ids_dump is not None:
        ids = load_ids_type(ids_dump)

    type_ = None
    type_dump = classification_vat_type_dump.find(f'{{{URI}}}classificationVATType')
    if type_dump is not None:
        type_ = pohoda_mserver_client.schema.xsd.load_string(type_dump)

    return ClassificationVatType(id_, ids, type_)


def load_currency_type(currency_type_dump):
    return pohoda_mserver_client.schema.xsd.load_double(currency_type_dump)


def load_dic_type(dic_type_dump):
    return pohoda_mserver_client.schema.xsd.load_string(dic_type_dump)


def load_document_number_type(document_number_type_dump):
    return pohoda_mserver_client.schema.xsd.load_string(document_number_type_dump)


def load_ic_dph_type(ic_dph_type_dump):
    return pohoda_mserver_client.schema.xsd.load_string(ic_dph_type_dump)


def load_ico_type(ico_type_dump):
    return pohoda_mserver_client.schema.xsd.load_string(ico_type_dump)


def load_id_type(id_type_dump):
    return pohoda_mserver_client.schema.xsd.load_integer(id_type_dump)


def load_ids_type(ids_type_dump):
    return pohoda_mserver_client.schema.xsd.load_string(ids_type_dump)


def load_liquidation_type(liquidation_type_dump):
    date = None
    date_dump = liquidation_type_dump.find(f'{{{URI}}}date')
    if date_dump is not None:
        date = pohoda_mserver_client.schema.xsd.load_date(date_dump)

    amount_home = None
    amount_home_dump = liquidation_type_dump.find(f'{{{URI}}}amountHome')
    if amount_home_dump is not None:
        amount_home = load_currency_type(amount_home_dump)

    amount_foreign = None
    amount_foreign_dump = liquidation_type_dump.find(f'{{{URI}}}amountForeign')
    if amount_foreign_dump is not None:
        amount_foreign = load_currency_type(amount_foreign_dump)

    return LiquidationType(date, amount_home, amount_foreign)


def load_my_address(my_address_dump):
    if my_address_dump.find(f'{{{URI}}}establishment') is not None:
        raise ValueError

    return load_address_internet_type(my_address_dump.find(f'{{{URI}}}address'))


def load_number_type(number_type_dump):
    id_ = None
    id_dump = number_type_dump.find(f'{{{URI}}}id')
    if id_dump is not None:
        id_ = load_id_type(id_dump)

    ids = None
    ids_dump = number_type_dump.find(f'{{{URI}}}ids')
    if ids_dump is not None:
        ids = load_ids_type(ids_dump)

    number_requested = None
    number_requested_dump = number_type_dump.find(f'{{{URI}}}numberRequested')
    if number_requested_dump is not None:
        if number_requested_dump.get('checkDuplicity') is not None:
            raise ValueError()
        number_requested = load_string32_not_empty(number_requested_dump)

    return NumberType(id_, ids, number_requested)


def load_payment_type(payment_type_dump):
    id_ = None
    id_dump = payment_type_dump.find(f'{{{URI}}}id')
    if id_dump is not None:
        id_ = load_id_type(id_dump)

    ids = None
    ids_dump = payment_type_dump.find(f'{{{URI}}}ids')
    if ids_dump is not None:
        ids = load_string20(ids_dump)

    type_ = None
    type_dump = payment_type_dump.find(f'{{{URI}}}paymentType')
    if type_dump is not None:
        type_ = pohoda_mserver_client.schema.xsd.load_string(type_dump)

    return PaymentType(id_, ids, type_)


def load_ref_type(ref_type_dump):
    id_ = None
    id_dump = ref_type_dump.find(f'{{{URI}}}id')
    if id_dump is not None:
        id_ = load_id_type(id_dump)

    ids = None
    ids_dump = ref_type_dump.find(f'{{{URI}}}ids')
    if ids_dump is not None:
        ids = load_ids_type(ids_dump)

    value_type = None
    value_type_dump = ref_type_dump.find(f'{{{URI}}}valueType')
    if value_type_dump is not None:
        value_type = pohoda_mserver_client.schema.xsd.load_string(value_type_dump)

    return RefType(id_, ids, value_type)


def load_stav_type(stav_type_dump):
    return pohoda_mserver_client.schema.xsd.load_string(stav_type_dump)


def load_string_company(string_company_dump):
    return pohoda_mserver_client.schema.xsd.load_string(string_company_dump)


def load_string10(string_dump):
    return pohoda_mserver_client.schema.xsd.load_string(string_dump)


def load_string15(string_dump):
    return pohoda_mserver_client.schema.xsd.load_string(string_dump)


def load_string20(string_dump):
    return pohoda_mserver_client.schema.xsd.load_string(string_dump)


def load_string24(string_dump):
    return pohoda_mserver_client.schema.xsd.load_string(string_dump)


def load_string240(string_dump):
    return pohoda_mserver_client.schema.xsd.load_string(string_dump)


def load_string32(string_dump):
    return pohoda_mserver_client.schema.xsd.load_string(string_dump)


def load_string32_not_empty(string_dump):
    return pohoda_mserver_client.schema.xsd.load_string(string_dump)


def load_string40(string_dump):
    return pohoda_mserver_client.schema.xsd.load_string(string_dump)


def load_string45(string_dump):
    return pohoda_mserver_client.schema.xsd.load_string(string_dump)


def load_string64(string_dump):
    return pohoda_mserver_client.schema.xsd.load_string(string_dump)


def load_string7(string_dump):
    return pohoda_mserver_client.schema.xsd.load_string(string_dump)


def load_string90(string_dump):
    return pohoda_mserver_client.schema.xsd.load_string(string_dump)


def load_string98(string_dump):
    return pohoda_mserver_client.schema.xsd.load_string(string_dump)


def load_sym_var_type(sym_var_type_dump):
    return pohoda_mserver_client.schema.xsd.load_string(sym_var_type_dump)


def load_type_currency_foreign(type_currency_foreign_dump):
    currency_dump = type_currency_foreign_dump.find(f'{{{URI}}}currency')
    currency = load_ref_type(currency_dump)

    rate = None
    rate_dump = type_currency_foreign_dump.find(f'{{{URI}}}rate')
    if rate_dump is not None:
        rate = pohoda_mserver_client.schema.xsd.load_float(rate_dump)

    amount = None
    amount_dump = type_currency_foreign_dump.find(f'{{{URI}}}amount')
    if amount_dump is not None:
        amount = pohoda_mserver_client.schema.xsd.load_integer(amount_dump)

    price_sum = None
    price_sum_dump = type_currency_foreign_dump.find(f'{{{URI}}}priceSum')
    if price_sum_dump is not None:
        price_sum = load_currency_type(price_sum_dump)

    return TypeCurrencyForeign(currency, rate, amount, price_sum)


def load_type_currency_foreign_item(type_currency_foreign_item_dump):
    unit_price = None
    unit_price_dump = type_currency_foreign_item_dump.find(f'{{{URI}}}unitPrice')
    if unit_price_dump is not None:
        unit_price = load_currency_type(unit_price_dump)

    price = None
    price_dump = type_currency_foreign_item_dump.find(f'{{{URI}}}price')
    if price_dump is not None:
        price = load_currency_type(price_dump)

    price_vat = None
    price_vat_dump = type_currency_foreign_item_dump.find(f'{{{URI}}}priceVAT')
    if price_vat_dump is not None:
        price_vat = load_currency_type(price_vat_dump)

    price_sum = None
    price_sum_dump = type_currency_foreign_item_dump.find(f'{{{URI}}}priceSum')
    if price_sum_dump is not None:
        price_sum = load_currency_type(price_sum_dump)

    return TypeCurrencyForeignItem(unit_price, price, price_vat, price_sum)


def load_type_currency_home(type_currency_home_dump):
    price_none = None
    price_none_dump = type_currency_home_dump.find(f'{{{URI}}}priceNone')
    if price_none_dump is not None:
        price_none = load_currency_type(price_none_dump)

    price_low = None
    price_low_dump = type_currency_home_dump.find(f'{{{URI}}}priceLow')
    if price_low_dump is not None:
        price_low = load_currency_type(price_low_dump)

    price_low_vat = None
    price_low_vat_dump = type_currency_home_dump.find(f'{{{URI}}}priceLowVAT')
    if price_low_vat_dump is not None:
        price_low_vat = load_currency_type(price_low_vat_dump)

    price_low_sum = None
    price_low_sum_dump = type_currency_home_dump.find(f'{{{URI}}}priceLowSum')
    if price_low_sum_dump is not None:
        price_low_sum = load_currency_type(price_low_sum_dump)

    price_high = None
    price_high_dump = type_currency_home_dump.find(f'{{{URI}}}priceHigh')
    if price_high_dump is not None:
        price_high = load_currency_type(price_high_dump)

    price_high_vat = None
    price_high_vat_dump = type_currency_home_dump.find(f'{{{URI}}}priceHighVAT')
    if price_high_vat_dump is not None:
        price_high_vat = load_currency_type(price_high_vat_dump)

    price_high_sum = None
    price_high_sum_dump = type_currency_home_dump.find(f'{{{URI}}}priceHighSum')
    if price_high_sum_dump is not None:
        price_high_sum = load_currency_type(price_high_sum_dump)

    price3 = None
    price3_dump = type_currency_home_dump.find(f'{{{URI}}}price3')
    if price3_dump is not None:
        price3 = load_currency_type(price3_dump)

    price3_vat = None
    price3_vat_dump = type_currency_home_dump.find(f'{{{URI}}}price3VAT')
    if price3_vat_dump is not None:
        price3_vat = load_currency_type(price3_vat_dump)

    price3_sum = None
    price3_sum_dump = type_currency_home_dump.find(f'{{{URI}}}price3Sum')
    if price3_sum_dump is not None:
        price3_sum = load_currency_type(price3_sum_dump)

    round = None
    round_dump = type_currency_home_dump.find(f'{{{URI}}}round')
    if round_dump is not None:
        round = load_type_round(round_dump)

    return TypeCurrencyHome(price_none, price_low, price_low_vat, price_low_sum, price_high, price_high_vat, price_high_sum, price3, price3_vat, price3_sum, round)


def load_type_currency_home_item(type_currency_home_item_dump):
    unit_price = None
    unit_price_dump = type_currency_home_item_dump.find(f'{{{URI}}}unitPrice')
    if unit_price_dump is not None:
        unit_price = load_currency_type(unit_price_dump)

    price = None
    price_dump = type_currency_home_item_dump.find(f'{{{URI}}}price')
    if price_dump is not None:
        price = load_currency_type(price_dump)

    price_vat = None
    price_vat_dump = type_currency_home_item_dump.find(f'{{{URI}}}priceVAT')
    if price_vat_dump is not None:
        price_vat = load_currency_type(price_vat_dump)

    price_sum = None
    price_sum_dump = type_currency_home_item_dump.find(f'{{{URI}}}priceSum')
    if price_sum_dump is not None:
        price_sum = load_currency_type(price_sum_dump)

    return TypeCurrencyHomeItem(unit_price, price, price_vat, price_sum)


def load_type_percentage(type_percentage_dump):
    return pohoda_mserver_client.schema.xsd.load_float(type_percentage_dump)


def load_type_round(type_round_dump):
    if type_round_dump.find(f'{{{URI}}}myGroupOfRound') is not None:
        raise ValueError()

    price_round_dump = type_round_dump.find(f'{{{URI}}}priceRound')
    return load_currency_type(price_round_dump)


def load_type_rounding_document(type_rounding_document_dump):
    return pohoda_mserver_client.schema.xsd.load_string(type_rounding_document_dump)


def load_type_rounding_vat(type_rounding_vat_dump):
    return pohoda_mserver_client.schema.xsd.load_string(type_rounding_vat_dump)


def load_unit_type(unit_type_dump):
    return pohoda_mserver_client.schema.xsd.load_string(unit_type_dump)


def load_vat_payer_type_type(vat_payer_type_type_dump):
    return pohoda_mserver_client.schema.xsd.load_string(vat_payer_type_type_dump)


def load_vat_rate_type(vat_rate_type_dump):
    return pohoda_mserver_client.schema.xsd.load_string(vat_rate_type_dump)


class AccountingType:

    def __init__(self, id_=None, ids=None, type_=None):
        self.id = id_
        self.ids = ids
        self.type = type_

    def __eq__(self, other):
        return (
            self.id == other.id and
            self.ids == other.ids and
            self.type == other.type)


class Address:

    def __init__(self, id_=None, address=None):
        self.id = id_
        self.address = address

    def __eq__(self, other):
        return (
            self.id == other.id and
            self.address == other.address)


class AddressInternetType:

    def __init__(self, company=None, title=None, surname=None, name=None, city=None, street=None, number=None, zip_=None, ico=None, dic=None, ic_dph=None, phone=None, mobil_phone=None, fax=None, email=None, www=None):
        self.company = company
        self.title = title
        self.surname = surname
        self.name = name
        self.city = city
        self.street = street
        self.number = number
        self.zip = zip_
        self.ico = ico
        self.dic = dic
        self.ic_dph = ic_dph
        self.phone = phone
        self.mobil_phone = mobil_phone
        self.fax = fax
        self.email = email
        self.www = www

    def __eq__(self, other):
        return (
            self.company == other.company and
            self.title == other.title and
            self.surname == other.surname and
            self.name == other.name and
            self.city == other.city and
            self.street == other.street and
            self.number == other.number and
            self.zip == other.zip and
            self.ico == other.ico and
            self.dic == other.dic and
            self.ic_dph == other.ic_dph and
            self.phone == other.phone and
            self.mobil_phone == other.mobil_phone and
            self.fax == other.fax and
            self.email == other.email and
            self.www == other.www)


class AddressType:

    def __init__(self, company=None, division=None, name=None, city=None, street=None, zip_=None, ico=None, dic=None, vat_payer_type=None, ic_dph=None, country=None, phone=None, mobil_phone=None, fax=None, email=None):
        self.company = company
        self.division = division
        self.name = name
        self.city = city
        self.street = street
        self.zip = zip_
        self.ico = ico
        self.dic = dic
        self.vat_payer_type = vat_payer_type
        self.ic_dph = ic_dph
        self.country = country
        self.phone = phone
        self.mobil_phone = mobil_phone
        self.fax = fax
        self.email = email

    def __eq__(self, other):
        return (
            self.company == other.company and
            self.division == other.division and
            self.name == other.name and
            self.city == other.city and
            self.street == other.street and
            self.zip == other.zip and
            self.ico == other.ico and
            self.dic == other.dic and
            self.vat_payer_type == other.vat_payer_type and
            self.ic_dph == other.ic_dph and
            self.country == other.country and
            self.phone == other.phone and
            self.mobil_phone == other.mobil_phone and
            self.fax == other.fax and
            self.email == other.email)


class ClassificationVatType:

    def __init__(self, id_=None, ids=None, type_=None):
        self.id = id_
        self.ids = ids
        self.type = type_

    def __eq__(self, other):
        return (
            self.id == other.id and
            self.ids == other.ids and
            self.type == other.type)


class LiquidationType:

    def __init__(self, date=None, amount_home=None, amount_foreign=None):
        self.date = date
        self.amount_home = amount_home
        self.amount_foreign = amount_foreign

    def __eq__(self, other):
        return (
            self.date == other.date and
            self.amount_home == other.amount_home and
            self.amount_foreign == other.amount_foreign)


class NumberType:

    def __init__(self, id_=None, ids=None, number_requested=None):
        self.id = id_
        self.ids = ids
        self.number_requested = number_requested

    def __eq__(self, other):
        return (
            self.id == other.id and
            self.ids == other.ids and
            self.number_requested == other.number_requested)


class PaymentType:

    def __init__(self, id_=None, ids=None, type_=None):
        self.id = id_
        self.ids = ids
        self.type = type_

    def __eq__(self, other):
        return (
            self.id == other.id and
            self.ids == other.ids and
            self.type == other.type)


class RefType:

    def __init__(self, id_=None, ids=None, value_type=None):
        self.id = id_
        self.ids = ids
        self.value_type = value_type


class TypeCurrencyForeign:

    def __init__(self, currency, rate=None, amount=None, price_sum=None):
        self.currency = currency
        self.rate = rate
        self.amount = amount
        self.price_sum = price_sum

    def __eq__(self, other):
        return (
            self.currency == other.currency and
            self.rate == other.rate and
            self.amount == other.amount and
            self.price_sum == other.price_sum)


class TypeCurrencyForeignItem:

    def __init__(self, unit_price=None, price=None, price_vat=None, price_sum=None):
        self.unit_price = unit_price
        self.price = price
        self.price_vat = price_vat
        self.price_sum = price_sum


class TypeCurrencyHome:

    def __init__(self, price_none=None, price_low=None, price_low_vat=None, price_low_sum=None, price_high=None, price_high_vat=None, price_high_sum=None, price3=None, price3_vat=None, price3_sum=None, round=None):
        self.price_none = price_none
        self.price_low = price_low
        self.price_low_vat = price_low_vat
        self.price_low_sum = price_low_sum
        self.price_high = price_high
        self.price_high_vat = price_high_vat
        self.price_high_sum = price_high_sum
        self.price3 = price3
        self.price3_vat = price3_vat
        self.price3_sum = price3_sum
        self.round = round

    def __eq__(self, other):
        return (
            self.price_none == other.price_none and
            self.price_low == other.price_low and
            self.price_low_vat == other.price_low_vat and
            self.price_low_sum == other.price_low_sum and
            self.price_high == other.price_high and
            self.price_high_vat == other.price_high_vat and
            self.price_high_sum == other.price_high_sum and
            self.price3 == other.price3 and
            self.price3_vat == other.price3_vat and
            self.price3_sum == other.price3_sum and
            self.round == other.round)


class TypeCurrencyHomeItem:

    def __init__(self, unit_price=None, price=None, price_vat=None, price_sum=None):
        self.unit_price = unit_price
        self.price = price
        self.price_vat = price_vat
        self.price_sum = price_sum
