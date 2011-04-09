#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
# This file is part of BfPy
#
# BfPy is a Python library to communicate with the Betfair Betting Exchange
# Copyright (C) 2010 Daniel Rodriguez (aka Daniel Rodriksson)
# Copyright (C) 2011 Sensible Odds Ltd.
#
# You can learn more and contact the author at:
#
#    http://code.google.com/p/bfpy/
#
# BfPy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BfPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BfPy. If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

'''
BfPy wsdsl variables holding the Betfair WSDL definitions
'''


#
# Variables containing the Betfair WSDL files
#
BFGlobalService = '''
<?xml version="1.0" encoding="UTF-8"?>

<!--

Copyright 2003-2004 The Sporting Exchange Limited. All rights reserved. 
The presentation, distribution or other dissemination of the information contained herein by The Sporting Exchange Limited (Betfair) is not a license, either expressly or impliedly, to any intellectual property owned or controlled by Betfair.
Save as provided by statute and to the fullest extent permitted by law, the following provisions set out the entire liability of Betfair (including any liability for the acts and omissions of its employees, agents and sub-contractors) to the User in respect of the use of its WSDL file whether in contract, tort, statute, equity or otherwise: 
(a)     The User acknowledges and agrees that (except as expressly provided in this Agreement) the WSDL is provided "AS IS" without warranties of any kind (whether express or implied);
(b)    All conditions, warranties, terms and undertakings (whether express or implied, statutory or otherwise relating to the delivery, performance, quality, uninterrupted use, fitness for purpose, occurrence or reliability of the WSDL are hereby excluded to the fullest extent permitted by law; and 
(c)     Betfair shall not be liable to the User for loss of profit (whether direct or indirect), loss of contracts or goodwill, lost advertising, loss of data or any type of special, indirect, consequential or economic loss (including loss or damage suffered by the User as a result of an action brought by a third party) even if such loss was reasonably foreseeable or Betfair had been advised of the possibility of the User incurring such loss.
No exclusion or limitation set out in this Agreement shall apply in the case of fraud or fraudulent concealment, death or personal injury resulting from the negligence of either party or any of its employees, agents or sub-contractors; and/or any breach of the obligations implied by (as appropriate) section 12 of the Sale of Goods Act 1979, section 2 of the Supply of Goods and Services Act 1982 or section 8 of the Supply of Goods (Implied Terms) Act 1973.

-->

<wsdl:definitions name="BFGlobalService"
  targetNamespace="http://www.betfair.com/publicapi/v3/BFGlobalService/"
  xmlns:types="http://www.betfair.com/publicapi/types/global/v3/"
  xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
  xmlns:tns="http://www.betfair.com/publicapi/v3/BFGlobalService/"
  xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <wsdl:types>
    <xsd:schema targetNamespace="http://www.betfair.com/publicapi/types/global/v3/">
      <xsd:import namespace="http://schemas.xmlsoap.org/soap/encoding/"/>
      <xsd:complexType name="LoginResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              	<xsd:element name="currency" nillable="true" type="xsd:string"/>
              	<xsd:element name="errorCode" type="types:LoginErrorEnum"/>
              	<xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              	<xsd:element name="validUntil" type="xsd:dateTime"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType abstract="true" name="APIResponse">
        <xsd:sequence>
          <xsd:element name="header" nillable="true" type="types:APIResponseHeader"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="APIResponseHeader">
        <xsd:sequence>
          <xsd:element name="errorCode" type="types:APIErrorEnum"/>
          <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
          <xsd:element name="sessionToken" nillable="true" type="xsd:string"/>
          <xsd:element name="timestamp" type="xsd:dateTime"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="APIErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INTERNAL_ERROR"/>
          <xsd:enumeration value="EXCEEDED_THROTTLE"/>
          <xsd:enumeration value="USER_NOT_SUBSCRIBED_TO_PRODUCT"/>
          <xsd:enumeration value="SUBSCRIPTION_INACTIVE_OR_SUSPENDED"/>
          <xsd:enumeration value="VENDOR_SOFTWARE_INACTIVE"/>
          <xsd:enumeration value="VENDOR_SOFTWARE_INVALID"/>
          <xsd:enumeration value="SERVICE_NOT_AVAILABLE_IN_PRODUCT"/>
          <xsd:enumeration value="NO_SESSION"/>
          <xsd:enumeration value="TOO_MANY_REQUESTS"/>
          <xsd:enumeration value="PRODUCT_REQUIRES_FUNDED_ACCOUNT"/>
          <xsd:enumeration value="SERVICE_NOT_AVAILABLE_FOR_LOGIN_STATUS"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:simpleType name="LoginErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="OK_MESSAGES"/>
          <xsd:enumeration value="FAILED_MESSAGE"/>
          <xsd:enumeration value="INVALID_USERNAME_OR_PASSWORD"/>
          <xsd:enumeration value="USER_NOT_ACCOUNT_OWNER"/>
          <xsd:enumeration value="INVALID_VENDOR_SOFTWARE_ID"/>
          <xsd:enumeration value="INVALID_PRODUCT"/>
          <xsd:enumeration value="INVALID_LOCATION"/>
          <xsd:enumeration value="LOGIN_FAILED_ACCOUNT_LOCKED"/>
          <xsd:enumeration value="ACCOUNT_SUSPENDED"/>
          <xsd:enumeration value="T_AND_C_ACCEPTANCE_REQUIRED"/>
          <xsd:enumeration value="POKER_T_AND_C_ACCEPTANCE_REQUIRED"/>
          <xsd:enumeration value="LOGIN_REQUIRE_TERMS_AND_CONDITIONS_ACCEPTANCE"/>
          <xsd:enumeration value="LOGIN_UNAUTHORIZED"/>
          <xsd:enumeration value="ACCOUNT_CLOSED"/>
          <xsd:enumeration value="LOGIN_RESTRICTED_LOCATION"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="LoginReq">
        <xsd:sequence>
          <xsd:element name="ipAddress" nillable="false" type="xsd:string"/>
          <xsd:element name="locationId" nillable="false" type="xsd:int"/>
          <xsd:element name="password" nillable="false" type="xsd:string"/>
          <xsd:element name="productId" nillable="false" type="xsd:int"/>
          <xsd:element name="username" nillable="false" type="xsd:string"/>
          <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="RetrieveLIMBMessageReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest"/>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="RetrieveLIMBMessageResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:RetrieveLIMBMessageErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="totalMessagesCount" nillable="false" type="xsd:int"/>
              <xsd:element name="retrievePersonalMessage" type="types:RetrievePersonalLIMBMessage"/>
              <xsd:element name="retrieveTCPrivacyPolicyChangeMessage" type="types:RetrieveTCPrivacyPolicyChangeLIMBMessage"/>
              <xsd:element name="retrievePasswordChangeMessage" type="types:RetrievePasswordChangeLIMBMessage"/>
              <xsd:element name="retrieveBirthDateCheckMessage" type="types:RetrieveBirthDateCheckLIMBMessage"/>
              <xsd:element name="retrieveAddressCheckMessage" type="types:RetrieveAddressCheckLIMBMessage"/>
              <xsd:element name="retrieveContactDetailsCheckMessage" type="types:RetrieveContactDetailsCheckLIMBMessage"/>
              <xsd:element name="retrieveChatNameChangeMessage" type="types:RetrieveChatNameChangeLIMBMessage"/>
              <xsd:element name="retrieveCardBillingAddressCheckItems" nillable="true" type="types:ArrayOfRetrieveCardBillingAddressCheckLIMBMessage"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:simpleType name="RetrieveLIMBMessageErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="RetrievePersonalLIMBMessage">
        <xsd:sequence>
          <xsd:element name="messageId" nillable="true" type="xsd:int"/>
          <xsd:element name="enforceDate" nillable="true" type="xsd:dateTime"/>
          <xsd:element name="indicator" nillable="false" type="xsd:boolean"/>
          <xsd:element name="message" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="RetrieveTCPrivacyPolicyChangeLIMBMessage">
        <xsd:sequence>
          <xsd:element name="messageId" nillable="true" type="xsd:int"/>
          <xsd:element name="enforceDate" nillable="true" type="xsd:dateTime"/>
          <xsd:element name="indicator" nillable="false" type="xsd:boolean"/>
          <xsd:element name="reasonForChange" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="RetrievePasswordChangeLIMBMessage">
        <xsd:sequence>
          <xsd:element name="messageId" nillable="true" type="xsd:int"/>
          <xsd:element name="enforceDate" nillable="true" type="xsd:dateTime"/>
          <xsd:element name="indicator" nillable="false" type="xsd:boolean"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="RetrieveBirthDateCheckLIMBMessage">
        <xsd:sequence>
          <xsd:element name="messageId" nillable="true" type="xsd:int"/>
          <xsd:element name="enforceDate" nillable="true" type="xsd:dateTime"/>
          <xsd:element name="indicator" nillable="false" type="xsd:boolean"/>
          <xsd:element name="birthDate" nillable="true" type="xsd:dateTime"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="RetrieveAddressCheckLIMBMessage">
        <xsd:sequence>
          <xsd:element name="messageId" nillable="true" type="xsd:int"/>
          <xsd:element name="enforceDate" nillable="true" type="xsd:dateTime"/>
          <xsd:element name="indicator" nillable="false" type="xsd:boolean"/>
          <xsd:element name="address1" type="xsd:string"/>
          <xsd:element name="address2" nillable="true" type="xsd:string"/>
          <xsd:element name="address3" nillable="true" type="xsd:string"/>
          <xsd:element name="town" nillable="true" type="xsd:string"/>
          <xsd:element name="county" nillable="true" type="xsd:string"/>
          <xsd:element name="zipCode" nillable="true" type="xsd:string"/>
          <xsd:element name="country" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="RetrieveContactDetailsCheckLIMBMessage">
        <xsd:sequence>
          <xsd:element name="messageId" nillable="true" type="xsd:int"/>
          <xsd:element name="enforceDate" nillable="true" type="xsd:dateTime"/>
          <xsd:element name="indicator" nillable="false" type="xsd:boolean"/>
          <xsd:element name="homeTelephone" nillable="true" type="xsd:string"/>
          <xsd:element name="workTelephone" nillable="true" type="xsd:string"/>
          <xsd:element name="mobileTelephone" nillable="true" type="xsd:string"/>
          <xsd:element name="emailAddress" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="RetrieveChatNameChangeLIMBMessage">
        <xsd:sequence>
          <xsd:element name="messageId" nillable="true" type="xsd:int"/>
          <xsd:element name="enforceDate" nillable="true" type="xsd:dateTime"/>
          <xsd:element name="indicator" nillable="false" type="xsd:boolean"/>
          <xsd:element name="chatName" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="ArrayOfRetrieveCardBillingAddressCheckLIMBMessage">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="3" minOccurs="0"
            name="retrieveCardBillingAddressCheckLIMBMessage" nillable="true" type="types:RetrieveCardBillingAddressCheckLIMBMessage"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="RetrieveCardBillingAddressCheckLIMBMessage">
        <xsd:sequence>
          <xsd:element name="messageId" nillable="true" type="xsd:int"/>
          <xsd:element name="enforceDate" nillable="true" type="xsd:dateTime"/>
          <xsd:element name="indicator" nillable="false" type="xsd:boolean"/>
          <xsd:element name="nickName" type="xsd:string"/>
          <xsd:element name="cardShortNumber" type="xsd:string"/>
          <xsd:element name="address1" type="xsd:string"/>
          <xsd:element name="address2" nillable="true" type="xsd:string"/>
          <xsd:element name="address3" nillable="true" type="xsd:string"/>
          <xsd:element name="town" nillable="true" type="xsd:string"/>
          <xsd:element name="county" nillable="true" type="xsd:string"/>
          <xsd:element name="zipCode" nillable="true" type="xsd:string"/>
          <xsd:element name="country" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="SubmitLIMBMessageReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="password" nillable="false" type="xsd:string"/>
              <xsd:element name="submitPersonalMessage" type="types:SubmitPersonalLIMBMessage"/>
              <xsd:element name="submitTCPrivacyPolicyChangeMessage" type="types:SubmitTCPrivacyPolicyChangeLIMBMessage"/>
              <xsd:element name="submitPasswordChangeMessage" type="types:SubmitPasswordChangeLIMBMessage"/>
              <xsd:element name="submitBirthDateCheckMessage" type="types:SubmitBirthDateCheckLIMBMessage"/>
              <xsd:element name="submitAddressCheckMessage" type="types:SubmitAddressCheckLIMBMessage"/>
              <xsd:element name="submitContactDetailsCheckMessage" type="types:SubmitContactDetailsCheckLIMBMessage"/>
              <xsd:element name="submitChatNameChangeMessage" type="types:SubmitChatNameChangeLIMBMessage"/>
              <xsd:element name="submitCardBillingAddressCheckItems" nillable="true" type="types:ArrayOfSubmitCardBillingAddressCheckLIMBMessage"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="SubmitPersonalLIMBMessage">
        <xsd:sequence>
          <xsd:element name="messageId" nillable="true" type="xsd:int"/>
          <xsd:element name="acknowledgment" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="SubmitTCPrivacyPolicyChangeLIMBMessage">
        <xsd:sequence>
          <xsd:element name="tCPrivacyPolicyChangeAcceptance" nillable="false" type="types:PrivacyPolicyChangeResponseEnum"/>
        </xsd:sequence>
      </xsd:complexType>
      
      <xsd:simpleType name="PrivacyPolicyChangeResponseEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="NO_REPLY"/>
          <xsd:enumeration value="ACCEPT"/>
          <xsd:enumeration value="REJECT"/>
        </xsd:restriction>
      </xsd:simpleType>
          
      <xsd:complexType name="SubmitPasswordChangeLIMBMessage">
        <xsd:sequence>
          <xsd:element name="messageId" nillable="true" type="xsd:int"/>
          <xsd:element name="newPassword" nillable="true" type="xsd:string"/>
          <xsd:element name="newPasswordRepeat" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="SubmitBirthDateCheckLIMBMessage">
        <xsd:sequence>
          <xsd:element name="messageId" nillable="true" type="xsd:int"/>
          <xsd:element name="detailsCorrect" nillable="true" type="xsd:string"/>
          <xsd:element name="correctBirthDate" nillable="true" type="xsd:dateTime"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="SubmitAddressCheckLIMBMessage">
        <xsd:sequence>
          <xsd:element name="messageId" nillable="true" type="xsd:int"/>
          <xsd:element name="detailsCorrect" nillable="true" type="xsd:string"/>
          <xsd:element name="newAddress1" nillable="true" type="xsd:string"/>
          <xsd:element name="newAddress2" nillable="true" type="xsd:string"/>
          <xsd:element name="newAddress3" nillable="true" type="xsd:string"/>
          <xsd:element name="newTown" nillable="true" type="xsd:string"/>
          <xsd:element name="newCounty" nillable="true" type="xsd:string"/>
          <xsd:element name="newZipCode" nillable="true" type="xsd:string"/>
          <xsd:element name="newCountry" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="SubmitContactDetailsCheckLIMBMessage">
        <xsd:sequence>
          <xsd:element name="messageId" nillable="true" type="xsd:int"/>
          <xsd:element name="detailsCorrect" nillable="true" type="xsd:string"/>
          <xsd:element name="newHomeTelephone" nillable="true" type="xsd:string"/>
          <xsd:element name="newWorkTelephone" nillable="true" type="xsd:string"/>
          <xsd:element name="newMobileTelephone" nillable="true" type="xsd:string"/>
          <xsd:element name="newEmailAddress" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="SubmitChatNameChangeLIMBMessage">
        <xsd:sequence>
          <xsd:element name="messageId" nillable="true" type="xsd:int"/>
          <xsd:element name="newChatName" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="ArrayOfSubmitCardBillingAddressCheckLIMBMessage">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="3" minOccurs="0"
            name="submitCardBillingAddressCheckLIMBMessage" nillable="true" type="types:SubmitCardBillingAddressCheckLIMBMessage"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="SubmitCardBillingAddressCheckLIMBMessage">
        <xsd:sequence>
          <xsd:element name="messageId" nillable="true" type="xsd:int"/>
          <xsd:element name="detailsCorrect" nillable="true" type="xsd:string"/>
          <xsd:element name="nickName" type="xsd:string"/>
          <xsd:element name="newAddress1" nillable="true" type="xsd:string"/>
          <xsd:element name="newAddress2" nillable="true" type="xsd:string"/>
          <xsd:element name="newAddress3" nillable="true" type="xsd:string"/>
          <xsd:element name="newTown" nillable="true" type="xsd:string"/>
          <xsd:element name="newCounty" nillable="true" type="xsd:string"/>
          <xsd:element name="newZipCode" nillable="true" type="xsd:string"/>
          <xsd:element name="newCountry" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="SubmitLIMBMessageResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:SubmitLIMBMessageErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="validationErrors" nillable="true" type="types:ArrayOfLIMBValidationErrorsEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:simpleType name="LIMBValidationErrorsEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="INVALID_DOB"/>
          <xsd:enumeration value="INVALID_ADDRESS_LINE1"/>
          <xsd:enumeration value="INVALID_ADDRESS_LINE2"/>
          <xsd:enumeration value="INVALID_ADDRESS_LINE3"/>
          <xsd:enumeration value="INVALID_CITY"/>
          <xsd:enumeration value="INVALID_COUNTY_STATE"/>
          <xsd:enumeration value="INVALID_COUNTRY_OF_RESIDENCE"/>
          <xsd:enumeration value="INVALID_POSTCODE"/>
          <xsd:enumeration value="INVALID_HOME_PHONE"/>
          <xsd:enumeration value="INVALID_WORK_PHONE"/>
          <xsd:enumeration value="INVALID_MOBILE_PHONE"/>
          <xsd:enumeration value="INVALID_EMAIL"/>
          <xsd:enumeration value="INVALID_PASSWORD"/>
          <xsd:enumeration value="RESERVED_PASSWORD"/>
          <xsd:enumeration value="INVALID_NEW_PASSWORD"/>
          <xsd:enumeration value="INVALID_TC_VERSION"/>
          <xsd:enumeration value="INVALID_PRIVICY_VERSION"/>
          <xsd:enumeration value="INVALID_CHATNAME"/>
          <xsd:enumeration value="CHATNAME_ALREADY_TAKEN"/>
          <xsd:enumeration value="INVALID_CARD_BILLING_ADDRESS_LINE_1"/>
          <xsd:enumeration value="INVALID_CARD_BILLING_ADDRESS_LINE_2"/>
          <xsd:enumeration value="INVALID_CARD_BILLING_ADDRESS_LINE_3"/>
          <xsd:enumeration value="INVALID_CARD_BILLING_CITY"/>
          <xsd:enumeration value="INVALID_CARD_BILLING_COUNTY_STATE"/>
          <xsd:enumeration value="INVALID_CARD_BILLING_ZIP_CODE"/>
          <xsd:enumeration value="INVALID_CARD_BILLING_COUNTRY_OF_RESIDENCE"/>
          <xsd:enumeration value="NO_SUCH_PERSONAL_MESSAGE"/>
          <xsd:enumeration value="NO_SUCH_TC_PRIVACY_POLICY_MESSAGE"/>
          <xsd:enumeration value="NO_SUCH_PASSWORD_CHANGE_MESSAGE"/>
          <xsd:enumeration value="NO_SUCH_BIRTH_DATE_CHECK_MESSAGE"/>
          <xsd:enumeration value="NO_SUCH_ADDRESS_CHECK_MESSAGE"/>
          <xsd:enumeration value="NO_SUCH_CONTACT_DETAILS_CHECK_MESSAGE"/>
          <xsd:enumeration value="NO_SUCH_CHATNAME_CHENGE_MESSAGE"/>
          <xsd:enumeration value="NO_SUCH_CARD_BILLING_ADDRESS_CHECK_MESSAGE"/>
          <xsd:enumeration value="INVALID_PERSONAL_MESSAGE_ACKNOWLEDGMENT"/>
          <xsd:enumeration value="INVALID_TC_PRIVACY_POLICY_MESSAGE_ACKNOWLEDGMENT"/>
          <xsd:enumeration value="INVALID_BIRTH_DATE_CHECK_MESSAGE"/>
          <xsd:enumeration value="INVALID_ADDRESS_CHECK_MESSAGE"/>
          <xsd:enumeration value="INVALID_CONTACT_DETAILS_CHECK_MESSAGE"/>
          <xsd:enumeration value="INVALID_CARD_BILLING_ADDRESS_CHECK_MESSAGE"/>

        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ArrayOfLIMBValidationErrorsEnum">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="LIMBValidationErrorsEnum" nillable="true" type="types:LIMBValidationErrorsEnum"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:simpleType name="SubmitLIMBMessageErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="VALIDATION_ERRORS"/>
          <xsd:enumeration value="INVALID_PASSWORD"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      
      <xsd:simpleType name="LogoutErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK" />
          <xsd:enumeration value="API_ERROR" />
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="LogoutResp">
        <xsd:complexContent mixed="false">
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string" />
              <xsd:element name="errorCode" type="types:LogoutErrorEnum" />
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="LogoutReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest" />
        </xsd:complexContent>
      </xsd:complexType>

      

      <xsd:complexType name="KeepAliveResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="apiVersion" nillable="true" type="xsd:string"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="KeepAliveReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest"/>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType abstract="true" name="APIRequest">
        <xsd:sequence>
          <xsd:element name="header" nillable="true" type="types:APIRequestHeader"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="APIRequestHeader">
        <xsd:sequence>
          <xsd:element name="clientStamp" type="xsd:long"/>
          <xsd:element name="sessionToken" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="GetEventsResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetEventsErrorEnum"/>
              <xsd:element name="eventItems" nillable="true" type="types:ArrayOfBFEvent"/>
              <xsd:element name="eventParentId" nillable="false" type="xsd:int"/>
              <xsd:element name="marketItems" nillable="true" type="types:ArrayOfMarketSummary"/>
              <xsd:element name="couponLinks" nillable="true" type="types:ArrayOfCouponLinks"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetEventsErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_EVENT_ID"/>
          <xsd:enumeration value="NO_RESULTS"/>
          <xsd:enumeration value="INVALID_LOCALE_DEFAULTING_TO_ENGLISH"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="BFEvent">
        <xsd:sequence>
          <xsd:element name="eventId" nillable="false" type="xsd:int"/>
          <xsd:element name="eventName" nillable="true" type="xsd:string"/>
          <xsd:element name="eventTypeId" nillable="false" type="xsd:int"/>
          <xsd:element name="menuLevel" nillable="false" type="xsd:int"/>
          <xsd:element name="orderIndex" nillable="false" type="xsd:int"/>
          <xsd:element name="startTime" type="xsd:dateTime"/>
          <xsd:element name="timezone" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfBFEvent">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="BFEvent" nillable="true" type="types:BFEvent"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="MarketSummary">
        <xsd:sequence>
          <xsd:element name="eventTypeId" nillable="false" type="xsd:int"/>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="marketName" nillable="true" type="xsd:string"/>
          <xsd:element name="marketType" type="types:MarketTypeEnum"/>
          <xsd:element name="marketTypeVariant" type="types:MarketTypeVariantEnum"/>
          <xsd:element name="menuLevel" nillable="false" type="xsd:int"/>
          <xsd:element name="orderIndex" nillable="false" type="xsd:int"/>
          <xsd:element name="startTime" type="xsd:dateTime"/>
          <xsd:element name="timezone" nillable="true" type="xsd:string"/>
          <xsd:element name="venue" nillable="true" type="xsd:string"/>  
          <xsd:element name="betDelay" nillable="false" type="xsd:int"/>
          <xsd:element name="numberOfWinners" nillable="false" type="xsd:int"/>
          <xsd:element name="eventParentId" nillable="false" type="xsd:int"/>
          <xsd:element name="exchangeId" nillable="false" type="xsd:int"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="MarketTypeEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="O"/>
          <xsd:enumeration value="L"/>
          <xsd:enumeration value="R"/>
          <xsd:enumeration value="A"/>
          <xsd:enumeration value="NOT_APPLICABLE"/>
        </xsd:restriction>
      </xsd:simpleType>
	  <xsd:simpleType name="MarketTypeVariantEnum">
        <xsd:restriction base="xsd:string">
		  <xsd:enumeration value="D"/><!-- default -->
          <xsd:enumeration value="ASL"/><!-- asian single line -->
          <xsd:enumeration value="ADL"/><!-- asian double line -->
          <xsd:enumeration value="COUP"/><!-- coupon -->
        </xsd:restriction>
      </xsd:simpleType>	  
      <xsd:complexType name="ArrayOfMarketSummary">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="MarketSummary" nillable="true" type="types:MarketSummary"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="CouponLink">
        <xsd:sequence>
          <xsd:element name="couponId" nillable="false" type="xsd:int"/>
          <xsd:element name="couponName" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfCouponLinks">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="CouponLink" nillable="true" type="types:CouponLink"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetEventsReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="eventParentId" nillable="false" type="xsd:int"/>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetEventTypesResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="eventTypeItems" nillable="true" type="types:ArrayOfEventType"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="errorCode" type="types:GetEventsErrorEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="EventType">
        <xsd:sequence>
          <xsd:element name="id" nillable="false" type="xsd:int"/>
          <xsd:element name="name" nillable="true" type="xsd:string"/>
          <xsd:element name="nextMarketId" nillable="false" type="xsd:int"/>          
          <xsd:element name="exchangeId" nillable="false" type="xsd:int"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfEventType">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="EventType" nillable="true" type="types:EventType"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetEventTypesReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:simpleType name="MarketStatusEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="ACTIVE"/>
          <xsd:enumeration value="INACTIVE"/>
          <xsd:enumeration value="CLOSED"/>
          <xsd:enumeration value="SUSPENDED"/>
        </xsd:restriction>
      </xsd:simpleType>
      
      <xsd:complexType name="Runner">
        <xsd:sequence>
          <xsd:element name="asianLineId" nillable="false" type="xsd:int"/>
          <xsd:element name="handicap" nillable="false" type="xsd:double"/>
          <xsd:element name="name" nillable="true" type="xsd:string"/>
          <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="GetSubscriptionInfoResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="subscriptions" nillable="true" type="types:ArrayOfSubscription"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="Subscription">
        <xsd:sequence>
          <xsd:element name="billingAmount" nillable="false" type="xsd:double"/>
          <xsd:element name="billingDate" type="xsd:dateTime"/>
          <xsd:element name="billingPeriod" type="types:BillingPeriodEnum"/>
          <xsd:element name="productId" nillable="false" type="xsd:int"/>
          <xsd:element name="productName" nillable="true" type="xsd:string"/>
          <xsd:element name="services" nillable="true" type="types:ArrayOfServiceCall"/>
          <xsd:element name="setupCharge" nillable="false" type="xsd:double"/>
          <xsd:element name="setupChargeActive" nillable="false" type="xsd:boolean"/>
          <xsd:element name="status" type="types:SubscriptionStatusEnum"/>
          <xsd:element name="subscribedDate" type="xsd:dateTime"/>
          <xsd:element name="vatEnabled" nillable="false" type="xsd:boolean"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="BillingPeriodEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="WEEKLY"/>
          <xsd:enumeration value="MONTHLY"/>
          <xsd:enumeration value="QUARTERLY"/>
          <xsd:enumeration value="ANNUALLY"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ServiceCall">
        <xsd:sequence>
          <xsd:element name="maxUsages" nillable="false" type="xsd:int"/>
          <xsd:element name="period" type="xsd:long"/>
          <xsd:element name="periodExpiry" type="xsd:dateTime"/>
          <xsd:element name="serviceType" type="types:ServiceEnum"/>
          <xsd:element name="usageCount" nillable="false" type="xsd:int"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="ServiceEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="ADD_PAYMENT_CARD"/>
          <xsd:enumeration value="DELETE_PAYMENT_CARD"/>
          <xsd:enumeration value="GET_PAYMENT_CARD"/>
          <xsd:enumeration value="UPDATE_PAYMENT_CARD"/>
          <xsd:enumeration value="LOGIN"/>
          <xsd:enumeration value="GET_BET"/>
          <xsd:enumeration value="PLACE_BETS"/>
          <xsd:enumeration value="WITHDRAW_TO_PAYMENT_CARD"/>
          <xsd:enumeration value="EDIT_BETS"/>
          <xsd:enumeration value="DEPOSIT_FROM_PAYMENT_CARD"/>
          <xsd:enumeration value="CANCEL_BETS"/>
          <xsd:enumeration value="DO_KEEP_ALIVE"/>
          <xsd:enumeration value="GET_ACCOUNT_STATEMENT"/>
          <xsd:enumeration value="LOAD_MARKET_PROFIT_LOSS"/>
          <xsd:enumeration value="GET_CURRENT_BETS"/>
          <xsd:enumeration value="LOAD_ACCOUNT_FUNDS"/>
          <xsd:enumeration value="LOAD_BET_HISTORY"/>
          <xsd:enumeration value="LOAD_DETAILED_AVAIL_MKT_DEPTH"/>
          <xsd:enumeration value="GET_MARKET_TRADED_VOLUME"/>
          <xsd:enumeration value="LOAD_EVENTS"/>
          <xsd:enumeration value="LOAD_EVENT_TYPES"/>
          <xsd:enumeration value="LOAD_MARKET"/>
          <xsd:enumeration value="LOAD_MARKET_PRICES"/>
          <xsd:enumeration value="LOAD_MARKET_PRICES_COMPRESSED"/>
          <xsd:enumeration value="LOAD_SERVICE_ANNOUNCEMENTS"/>
          <xsd:enumeration value="LOAD_SUBSCRIPTION_INFO"/>
          <xsd:enumeration value="CREATE_ACCOUNT"/>
          <xsd:enumeration value="CONVERT_CURRENCY"/>
          <xsd:enumeration value="GET_CURRENCIES"/>
          <xsd:enumeration value="FORGOT_PASSWORD"/>
		  <xsd:enumeration value="MODIFY_PASSWORD"/>
          <xsd:enumeration value="VIEW_PROFILE"/>
          <xsd:enumeration value="MODIFY_PROFILE"/>
          <xsd:enumeration value="LOGOUT"/>
          <xsd:enumeration value="RETRIEVE_LIMB_MESSAGE"/>
          <xsd:enumeration value="SUBMIT_LIMB_MESSAGE"/>
          <xsd:enumeration value="GET_MARGIN_MARKET_PRICES"/>
          <xsd:enumeration value="GET_MARGIN_MARKET_PRICES_COMPRESSED"/>
          <xsd:enumeration value="GENERATE_REGISTERED_MARGIN_PRICES"/>
          <xsd:enumeration value="MARGINLOGIN"/>
          <xsd:enumeration value="TRANSFER_FUNDS"/>
          <xsd:enumeration value="ADD_VENDORSUBSCRIPTION"/>
          <xsd:enumeration value="UPDATE_VENDORSUBSCRIPTION"/>
          <xsd:enumeration value="CANCEL_VENDORSUBSCRIPTION"/>
          <xsd:enumeration value="GET_VENDOR_USERS"/>
          <xsd:enumeration value="GET_VENDORSUBSCRIPTION_INFO"/>
          <xsd:enumeration value="GET_VENDOR_INFO"/>
          
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ArrayOfServiceCall">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="ServiceCall" nillable="true" type="types:ServiceCall"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="SubscriptionStatusEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="ACTIVE"/>
          <xsd:enumeration value="INACTIVE"/>
          <xsd:enumeration value="SUSPENDED"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ArrayOfSubscription">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="Subscription" nillable="true" type="types:Subscription"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetSubscriptionInfoReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest"/>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="DepositFromPaymentCardResp">
      <xsd:annotation>
		  <xsd:documentation>
			  Result of a DepositFromPaymentCardReq.  If errorCode is set to CARD_AMOUNT_OUTSIDE_LIMIT then minAmount and maxAmount 
			  will be set.  If errorCode is set to DEPOSIT_LIMIT_EXCEEDED then maxAmount will be set.
		  </xsd:documentation>
      </xsd:annotation>
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:PaymentsErrorEnum"/>
              <xsd:element name="fee" nillable="false" type="xsd:double"/>
              <xsd:element name="maxAmount" nillable="false" type="xsd:double"/>
              <xsd:element name="minAmount" nillable="false" type="xsd:double"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="netAmount" nillable="false" type="xsd:double"/>
              <xsd:element name="transactionId" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="PaymentsErrorEnum">
        <xsd:restriction base="xsd:string">
	        <xsd:enumeration value="OK"/>
			<xsd:enumeration value="ACCOUNT_SUSPENDED"/>
			<xsd:enumeration value="API_ERROR"/>
			<xsd:enumeration value="CARD_AMOUNT_OUTSIDE_LIMIT"/>
			<xsd:enumeration value="CARD_EXPIRED"/>
			<xsd:enumeration value="CARD_LOCKED"/>
			<xsd:enumeration value="CARD_NOT_FOUND"/>
			<xsd:enumeration value="DEPOSIT_DECLINED"/>
			<xsd:enumeration value="DEPOSIT_LIMIT_EXCEEDED"/>
			<xsd:enumeration value="EXCEEDS_BALANCE"/>
			<xsd:enumeration value="CARD_NOT_VALIDATED"/>
			<xsd:enumeration value="INVALID_AMOUNT"/>
			<xsd:enumeration value="INVALID_CARD_CV2"/>
			<xsd:enumeration value="INVALID_CARD_DETAILS"/>
			<xsd:enumeration value="INVALID_EXPIRY_DATE"/>
			<xsd:enumeration value="INVALID_MASTERCARD"/>
			<xsd:enumeration value="INVALID_PASSWORD"/>
			<xsd:enumeration value="CFT_MAX_WITHDRAWAL_LIMIT"/>
			<xsd:enumeration value="NEGATIVE_NET_DEPOSITS"/>
			<xsd:enumeration value="NON_STERLING_TO_UK_MASTERCARD"/>
			<xsd:enumeration value="NON_ZERO_NON_NEG_NET_DEPOSITS"/>
			<xsd:enumeration value="UNAUTHORIZED"/>
			<xsd:enumeration value="VISA_WITHDRAWAL_NOT_POSSIBLE"/>
			<xsd:enumeration value="DUPLICATE_WITHDRAWAL"/>			        
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="DepositFromPaymentCardReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="amount" nillable="false" type="xsd:double"/>
              <xsd:element name="cardIdentifier" nillable="true" type="xsd:string"/>
              <xsd:element name="cv2" nillable="true" type="xsd:string"/>
              <xsd:element name="password" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="AddPaymentCardReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="cardNumber" type="xsd:string"/>
              <xsd:element name="cardType" type="types:CardTypeEnum"/>
              <xsd:element name="startDate" nillable="true" type="xsd:string"/>
              <xsd:element name="expiryDate" type="xsd:string"/>
              <xsd:element name="issueNumber" nillable="true" type="xsd:string"/>
              <xsd:element name="billingName" type="xsd:string"/>
              <xsd:element name="nickName" type="xsd:string"/>
              <xsd:element name="password" type="xsd:string"/>
              <xsd:element name="address1" type="xsd:string"/>
              <xsd:element name="address2" nillable="true" type="xsd:string"/>
              <xsd:element name="address3" nillable="true" type="xsd:string"/>
              <xsd:element name="address4" nillable="true" type="xsd:string"/>
              <xsd:element name="town" nillable="true" type="xsd:string"/>
              <xsd:element name="county" nillable="true" type="xsd:string"/>
              <xsd:element name="zipCode" nillable="true" type="xsd:string"/>
              <xsd:element name="country" nillable="true" type="xsd:string"/>
              <xsd:element name="cardStatus" type="types:PaymentCardStatusEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="DeletePaymentCardReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="nickName" type="xsd:string"/>
              <xsd:element name="password" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="GetPaymentCardReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="UpdatePaymentCardReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="nickName" type="xsd:string"/>
              <xsd:element name="password" type="xsd:string"/>
              <xsd:element name="expiryDate" nillable="true" type="xsd:string"/>
              <xsd:element name="startDate" nillable="true" type="xsd:string"/>
              <xsd:element name="issueNumber" nillable="true" type="xsd:string"/>
              <xsd:element name="address1" nillable="true" type="xsd:string"/>
              <xsd:element name="address2" nillable="true" type="xsd:string"/>
              <xsd:element name="address3" nillable="true" type="xsd:string"/>
              <xsd:element name="address4" nillable="true" type="xsd:string"/>
              <xsd:element name="town" nillable="true" type="xsd:string"/>
              <xsd:element name="county" nillable="true" type="xsd:string"/>
              <xsd:element name="zipCode" nillable="true" type="xsd:string"/>
              <xsd:element name="country" nillable="true" type="xsd:string"/>
              <xsd:element name="cardStatus" type="types:PaymentCardStatusEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:simpleType name="CardTypeEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="VISA"/>
          <xsd:enumeration value="MASTERCARD"/>
          <xsd:enumeration value="VISADELTA"/>
          <xsd:enumeration value="SWITCH"/>
          <xsd:enumeration value="SOLO"/>
          <xsd:enumeration value="ELECTRON"/>
          <xsd:enumeration value="LASER"/>
          <xsd:enumeration value="MAESTRO"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="AddPaymentCardResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:AddPaymentCardErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="paymentCard" type="types:PaymentCard"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:simpleType name="AddPaymentCardErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_CARD_DETAILS"/>
          <xsd:enumeration value="INVALID_CARD_CV2"/>
          <xsd:enumeration value="INVALID_PASSWORD"/>
          <xsd:enumeration value="ACCOUNT_INACTIVE"/>
          <xsd:enumeration value="UNAUTHORIZED"/>
          <xsd:enumeration value="INVALID_EXPIRY_DATE"/>
          <xsd:enumeration value="INVALID_START_DATE"/>
          <xsd:enumeration value="INVALID_CARD_NUMBER"/>
          <xsd:enumeration value="INVALID_ZIP_CODE"/>
          <xsd:enumeration value="INVALID_COUNTRY_CODE"/>
          <xsd:enumeration value="INVALID_BILLING_NAME"/>
          <xsd:enumeration value="INVALID_CARD_ADDRESS"/>
          <xsd:enumeration value="CARD_ALREADY_EXISTS"/>
          <xsd:enumeration value="AGE_VERIFICATION_REQUIRED"/>
          <xsd:enumeration value="NOT_FUNDED_WITH_FIRST_CARD"/>
          <xsd:enumeration value="CARD_NOT_VALID_FOR_ACCOUNT_CURRENCY"/>
          <xsd:enumeration value="INVALID_CARD_TYPE"/>
          <xsd:enumeration value="MAXIMUM_NUMBER_OF_CARDS_REACHED"/>
          <xsd:enumeration value="INVALID_ISSUE_NUMBER"/>          
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:simpleType name="DeletePaymentCardErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_CARD_DETAILS"/>
          <xsd:enumeration value="INVALID_PASSWORD"/>
          <xsd:enumeration value="ACCOUNT_INACTIVE"/>
          <xsd:enumeration value="UNAUTHORIZED"/>
          <xsd:enumeration value="CARD_NOT_DELETED"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="DeletePaymentCardResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:DeletePaymentCardErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="nickName" type="xsd:string"/>
              <xsd:element name="billingName" type="xsd:string"/>
              <xsd:element name="cardShortNumber" type="xsd:string"/>
              <xsd:element name="cardType" type="types:CardTypeEnum"/>
              <xsd:element name="issuingCountry" nillable="true" type="xsd:string"/>
              <xsd:element name="expiryDate" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="UpdatePaymentCardResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:UpdatePaymentCardErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="nickName" type="xsd:string"/>
              <xsd:element name="billingName" type="xsd:string"/>
              <xsd:element name="cardType" type="types:CardTypeEnum"/>
              <xsd:element name="expiryDate" type="xsd:string"/>
              <xsd:element name="startDate" nillable="true" type="xsd:string"/>
              <xsd:element name="address1" type="xsd:string"/>
              <xsd:element name="address2" nillable="true" type="xsd:string"/>
              <xsd:element name="address3" nillable="true" type="xsd:string"/>
              <xsd:element name="address4" nillable="true" type="xsd:string"/>
              <xsd:element name="zipCode" nillable="true" type="xsd:string"/>
              <xsd:element name="country" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:simpleType name="UpdatePaymentCardErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_CARD_DETAILS"/>
          <xsd:enumeration value="INVALID_PASSWORD"/>
          <xsd:enumeration value="ACCOUNT_INACTIVE"/>
          <xsd:enumeration value="UNAUTHORIZED"/>
          <xsd:enumeration value="INVALID_COUNTRY_CODE"/>
          <xsd:enumeration value="INVALID_CARD_ADDRESS"/>
          <xsd:enumeration value="INVALID_EXPIRY_DATE"/>
          <xsd:enumeration value="INVALID_START_DATE"/>
          <xsd:enumeration value="INVALID_ZIP_CODE"/>
          <xsd:enumeration value="INVALID_ISSUE_NUMBER"/>                    
          <xsd:enumeration value="API_ERROR"/>
          <xsd:enumeration value="CARD_NOT_FOUND"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="GetPaymentCardResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetPaymentCardErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="paymentCardItems" nillable="true" type="types:ArrayOfPaymentCard"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:simpleType name="GetPaymentCardErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_PASSWORD"/>
          <xsd:enumeration value="ACCOUNT_INACTIVE"/>
          <xsd:enumeration value="UNAUTHORIZED"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="PaymentCard">
        <xsd:sequence>
          <xsd:element name="nickName" type="xsd:string"/>
          <xsd:element name="cardShortNumber" type="xsd:string"/>
          <xsd:element name="expiryDate" type="xsd:string"/>
          <xsd:element name="startDate" nillable="true" type="xsd:string"/>
          <xsd:element name="issueNumber" nillable="true" type="xsd:string"/>
          <xsd:element name="cardType" type="types:CardTypeEnum"/>
          <xsd:element name="issuingCountryIso3" nillable="true" type="xsd:string"/>
          <xsd:element name="totalDeposits" nillable="true" type="xsd:double"/>
          <xsd:element name="totalWithdrawals" nillable="true" type="xsd:double"/>
          <xsd:element name="netDeposits" nillable="true" type="xsd:double"/>
          <xsd:element name="validationStatus" nillable="true" type="xsd:string"/>
          <xsd:element name="billingName" type="xsd:string"/>          
		  <xsd:element name="billingAddress1" nillable="true" type="xsd:string"/>
		  <xsd:element name="billingAddress2" nillable="true" type="xsd:string"/>
		  <xsd:element name="billingAddress3" nillable="true" type="xsd:string"/>
		  <xsd:element name="billingAddress4" nillable="true" type="xsd:string"/>
		  <xsd:element name="town" nillable="true" type="xsd:string"/>
		  <xsd:element name="county" nillable="true" type="xsd:string"/>
		  <xsd:element name="postcode" nillable="true" type="xsd:string"/>
		  <xsd:element name="billingCountryIso3" nillable="true" type="xsd:string"/>
		  <xsd:element name="cardStatus" type="types:PaymentCardStatusEnum"/>
        </xsd:sequence>
      </xsd:complexType>
	  
	  <xsd:simpleType name="PaymentCardStatusEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="LOCKED"/>
          <xsd:enumeration value="UNLOCKED"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="ArrayOfPaymentCard">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="PaymentCard" nillable="true" type="types:PaymentCard"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="WithdrawToPaymentCardResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="amountWithdrawn" nillable="false" type="xsd:double"/>
              <xsd:element name="errorCode" type="types:PaymentsErrorEnum"/>
              <xsd:element name="maxAmount" nillable="false" type="xsd:double"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="WithdrawToPaymentCardReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="amount" nillable="false" type="xsd:double"/>
              <xsd:element name="cardIdentifier" nillable="true" type="xsd:string"/>
              <xsd:element name="password" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="TransferFundsReq">
      	<xsd:complexContent>
      		<xsd:extension base="types:APIRequest">
      			<xsd:sequence>
	          		<xsd:element name="sourceWalletId" nillable="false" type="xsd:int" />
	          		<xsd:element name="targetWalletId" nillable="false" type="xsd:int" />	          		
      				<xsd:element name="amount" nillable="false" type="xsd:double" />
      			</xsd:sequence>
      		</xsd:extension>
      	</xsd:complexContent>
      </xsd:complexType>
     <xsd:complexType name="TransferFundsResp">
      	<xsd:complexContent>
      		<xsd:extension base="types:APIResponse">
      			<xsd:sequence>
      				<xsd:element name="errorCode" nillable="false" type="types:TransferFundsErrorEnum" />
                    <xsd:element name="minorErrorCode" nillable="true" type="xsd:string" />
      				<xsd:element name="monthlyDepositTotal" nillable="true" type="xsd:double" />
      			</xsd:sequence>
      		</xsd:extension>
      	</xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="TransferFundsErrorEnum">
      	<xsd:restriction base="xsd:string">
      		<xsd:enumeration value="OK" />
      		<xsd:enumeration value="INVALID_AMOUNT" />
			<xsd:enumeration value="TRANSFER_FAILED"/>   
			<xsd:enumeration value="OVER_BALANCE"/>   
      		<xsd:enumeration value="WALLETS_MUST_BE_DIFFERENT"/>         		   		
          	<xsd:enumeration value="SOURCE_WALLET_UNKNOWN" />
          	<xsd:enumeration value="SOURCE_WALLET_SUSPENDED" />
          	<xsd:enumeration value="SOURCE_WALLET_SUSPENDED_KYC" />
  	        <xsd:enumeration value="SOURCE_WALLET_KYC_WITHDRAWAL" />
  	        <xsd:enumeration value="SOURCE_WALLET_KYC_DEPOSIT_TOTAL" />
   	        <xsd:enumeration value="SOURCE_WALLET_KYC_DEPOSIT_MONTH" />
          	<xsd:enumeration value="TARGET_WALLET_UNKNOWN" />
          	<xsd:enumeration value="TARGET_WALLET_SUSPENDED" />
          	<xsd:enumeration value="TARGET_WALLET_SUSPENDED_KYC" />
  	        <xsd:enumeration value="TARGET_WALLET_KYC_WITHDRAWAL" />
  	        <xsd:enumeration value="TARGET_WALLET_KYC_DEPOSIT_TOTAL" />
   	        <xsd:enumeration value="TARGET_WALLET_KYC_DEPOSIT_MONTH" />
      		<xsd:enumeration value="API_ERROR" />
      	</xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="SelfExcludeReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="selfExclude" nillable="false" type="xsd:boolean"/>
              <xsd:element name="password" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="SelfExcludeResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string" />
              <xsd:element name="errorCode" type="types:SelfExcludeErrorEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="SelfExcludeErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="ACCOUNT_CLOSED"/>
          <xsd:enumeration value="INVALID_PASSWORD"/>
          <xsd:enumeration value="INVALID_SELF_EXCLUDE_VALUE"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      
      <xsd:complexType name="ConvertCurrencyResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="convertedAmount" nillable="false" type="xsd:double"/>
              <xsd:element name="errorCode" type="types:ConvertCurrencyErrorEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="ConvertCurrencyErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_AMOUNT"/>
          <xsd:enumeration value="INVALID_FROM_CURRENCY"/>
          <xsd:enumeration value="INVALID_TO_CURRENCY"/>
          <xsd:enumeration value="CANNOT_CONVERT"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ConvertCurrencyReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="amount" nillable="false" type="xsd:double"/>
              <xsd:element name="fromCurrency" nillable="true" type="xsd:string"/>
              <xsd:element name="toCurrency" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetCurrenciesResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="currencyItems" nillable="true" type="types:ArrayOfCurrency"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="Currency">
        <xsd:sequence>
          <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
          <xsd:element name="rateGBP" nillable="false" type="xsd:double"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfCurrency">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="Currency" nillable="true" type="types:Currency"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetCurrenciesReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest"/>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="GetCurrenciesV2Resp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="currencyItems" nillable="true" type="types:ArrayOfCurrencyV2"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="CurrencyV2">
        <xsd:complexContent>
          <xsd:extension base="types:Currency">
            <xsd:sequence>
              <!-- Version 2 fields -->
              <xsd:element name="minimumStake" nillable="true" type="xsd:double"/>
              <xsd:element name="minimumRangeStake" nillable="true" type="xsd:double"/>
              <xsd:element name="minimumBSPLayLiability" nillable="true" type="xsd:double"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfCurrencyV2">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="CurrencyV2" nillable="true" type="types:CurrencyV2"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetCurrenciesV2Req">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest"/>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="ViewReferAndEarnReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest"/>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="ViewReferAndEarnResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="errorCode" type="types:ViewReferAndEarnErrorEnum"/>
              <xsd:element name="referAndEarnCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="ViewReferAndEarnErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="NO_RESULTS"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="ViewProfileReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest"/>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="ViewProfileResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="errorCode" type="types:ViewProfileErrorEnum"/>
              <xsd:element name="title" type="types:TitleEnum"/>
              <xsd:element name="firstName" nillable="true" type="xsd:string"/>
              <xsd:element name="surname" nillable="true" type="xsd:string"/>
              <xsd:element name="userName" nillable="true" type="xsd:string"/>
              <xsd:element name="forumName" nillable="true" type="xsd:string"/>
              <xsd:element name="address1" nillable="true" type="xsd:string"/>
              <xsd:element name="address2" nillable="true" type="xsd:string"/>
              <xsd:element name="address3" nillable="true" type="xsd:string"/>
              <xsd:element name="townCity" nillable="true" type="xsd:string"/>
              <xsd:element name="countyState" nillable="true" type="xsd:string"/>
              <xsd:element name="postCode" nillable="true" type="xsd:string"/>
              <xsd:element name="countryOfResidence" nillable="true" type="xsd:string"/>
              <xsd:element name="homeTelephone" nillable="true" type="xsd:string"/>
              <xsd:element name="workTelephone" nillable="true" type="xsd:string"/>
              <xsd:element name="mobileTelephone" nillable="true" type="xsd:string"/>
              <xsd:element name="emailAddress" nillable="true" type="xsd:string"/>
              <xsd:element name="timeZone" nillable="true" type="xsd:string"/>
              <xsd:element name="currency" nillable="true" type="xsd:string"/>
              <xsd:element name="gamcareLimit" nillable="true" type="xsd:int"/>
              <xsd:element name="gamcareFrequency" type="types:GamcareLimitFreqEnum"/>
              <xsd:element name="gamcareLossLimit" nillable="true" type="xsd:int"/>
              <xsd:element name="gamcareLossLimitFrequency" type="types:GamcareLimitFreqEnum"/>
              <xsd:element name="gamcareUpdateDate" type="xsd:dateTime"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="ViewProfileV2Req">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest"/>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="ViewProfileV2Resp">
        <xsd:complexContent>
          <xsd:extension base="types:ViewProfileResp">
            <xsd:sequence>
              <!-- Version 2 Fields -->
              <xsd:element name="tAN" nillable="true" type="xsd:string"/>
              <xsd:element name="referAndEarnCode" nillable="true" type="xsd:string"/>
              <xsd:element name="earthportID" nillable="true" type="xsd:string"/>
              <xsd:element name="kYCStatus" type="types:KYCStatusEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:simpleType name="ViewProfileErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="UNAUTHORIZED"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="ModifyProfileReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="password" nillable="false" type="xsd:string"/>
              <xsd:element name="address1" nillable="true" type="xsd:string"/>
              <xsd:element name="address2" nillable="true" type="xsd:string"/>
              <xsd:element name="address3" nillable="true" type="xsd:string"/>
              <xsd:element name="townCity" nillable="true" type="xsd:string"/>
              <xsd:element name="countyState" nillable="true" type="xsd:string"/>
              <xsd:element name="postCode" nillable="true" type="xsd:string"/>
              <xsd:element name="countryOfResidence" nillable="true" type="xsd:string"/>
              <xsd:element name="homeTelephone" nillable="true" type="xsd:string"/>
              <xsd:element name="workTelephone" nillable="true" type="xsd:string"/>
              <xsd:element name="mobileTelephone" nillable="true" type="xsd:string"/>
              <xsd:element name="emailAddress" nillable="true" type="xsd:string"/>
              <xsd:element name="timeZone" nillable="true" type="xsd:string"/>
              <xsd:element name="depositLimit" nillable="true" type="xsd:int"/>
              <xsd:element name="depositLimitFrequency" type="types:GamcareLimitFreqEnum"/>
              <xsd:element name="lossLimit" nillable="true" type="xsd:int"/>
              <xsd:element name="lossLimitFrequency" type="types:GamcareLimitFreqEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="ModifyProfileResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:ModifyProfileErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="validationErrors"
                nillable="true" type="types:ArrayOfValidationErrorsEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:simpleType name="ModifyProfileErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="VALIDATION_ERRORS"/>
          <xsd:enumeration value="PROFILE_MODIFICATION_ERROR"/>
          <xsd:enumeration value="UNAUTHORIZED"/>
          <xsd:enumeration value="INVALID_PASSWORD"/>
          <xsd:enumeration value="ACCOUNT_INACTIVE"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="CreateAccountResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="accountId" nillable="false" type="xsd:int"/>
              <xsd:element name="accountStatus" type="types:AccountStatusEnum"/>
              <xsd:element name="errorCode" type="types:CreateAccountErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="tan" nillable="true" type="xsd:string"/>
              <xsd:element name="userId" nillable="false" type="xsd:int"/>
              <xsd:element name="validationErrors"
                nillable="true" type="types:ArrayOfValidationErrorsEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="AccountStatusEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="A"/>
          <xsd:enumeration value="C"/>
          <xsd:enumeration value="D"/>
          <xsd:enumeration value="L"/>
          <xsd:enumeration value="P"/>
          <xsd:enumeration value="S"/>
          <xsd:enumeration value="T"/>
          <xsd:enumeration value="X"/>
          <xsd:enumeration value="Z"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:simpleType name="CreateAccountErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="VALIDATION_ERRORS"/>
          <xsd:enumeration value="ACCOUNT_CREATION_ERROR"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:simpleType name="ValidationErrorsEnum">
        <xsd:restriction base="xsd:string">
			<xsd:enumeration value="DUPLICATE_USERNAME"/>
			<xsd:enumeration value="FUNDS_TRANSFER_CANCEL"/>
			<xsd:enumeration value="FUNDS_TRANSFER_CURRENCY_MISMATCH"/>
			<xsd:enumeration value="INCOMPLETE_DETAILS"/>
			<xsd:enumeration value="INSUFFICIENT_FUNDS"/>
			<xsd:enumeration value="INVALID_ACCOUNT_TYPE"/>
			<xsd:enumeration value="INVALID_ADDRESS_LINE1"/>
			<xsd:enumeration value="INVALID_ADDRESS_LINE2"/>
			<xsd:enumeration value="INVALID_ADDRESS_LINE3"/>
			<xsd:enumeration value="INVALID_ANSWER1"/>
			<xsd:enumeration value="INVALID_ANSWER2"/>
			<xsd:enumeration value="INVALID_BROWSER"/>
			<xsd:enumeration value="INVALID_CITY"/>
			<xsd:enumeration value="INVALID_COUNTRY_OF_RESIDENCE"/>
			<xsd:enumeration value="INVALID_COUNTY_STATE"/>
			<xsd:enumeration value="INVALID_CURRENCY"/>
			<xsd:enumeration value="INVALID_DEPOSIT_LIMIT"/>
			<xsd:enumeration value="INVALID_DEPOSIT_LIMIT_FREQUENCY"/>
			<xsd:enumeration value="INVALID_DETAILS"/>
			<xsd:enumeration value="INVALID_DOB"/>
			<xsd:enumeration value="INVALID_EMAIL"/>
			<xsd:enumeration value="INVALID_FIRSTNAME"/>
			<xsd:enumeration value="INVALID_GENDER"/>
			<xsd:enumeration value="INVALID_HOME_PHONE"/>
			<xsd:enumeration value="INVALID_IP_ADDRESS"/>
			<xsd:enumeration value="INVALID_LANGUAGE"/>
			<xsd:enumeration value="INVALID_LOCALE"/>
			<xsd:enumeration value="INVALID_LOSS_LIMIT"/>
			<xsd:enumeration value="INVALID_LOSS_LIMIT_FREQUENCY"/>
			<xsd:enumeration value="INVALID_MASTER_ID"/>
			<xsd:enumeration value="INVALID_MOBILE_PHONE"/>
			<xsd:enumeration value="INVALID_PARTNERID"/>
			<xsd:enumeration value="INVALID_PASSWORD"/>
			<xsd:enumeration value="INVALID_POSTCODE"/>
			<xsd:enumeration value="INVALID_PRIVICY_VERSION"/>
			<xsd:enumeration value="INVALID_PRODUCT_ID"/>
			<xsd:enumeration value="INVALID_REFERRER_CODE"/>
			<xsd:enumeration value="INVALID_REGION"/>
			<xsd:enumeration value="INVALID_SECURITY_QUESTION1"/>
			<xsd:enumeration value="INVALID_SECURITY_QUESTION2"/>
			<xsd:enumeration value="INVALID_SUBPARTNERID"/>
			<xsd:enumeration value="INVALID_SUPERPARTNERID"/>
			<xsd:enumeration value="INVALID_SURNAME"/>
			<xsd:enumeration value="INVALID_TC_VERSION"/>
			<xsd:enumeration value="INVALID_TIMEZONE"/>
			<xsd:enumeration value="INVALID_TITLE"/>
			<xsd:enumeration value="INVALID_USERNAME"/>
			<xsd:enumeration value="INVALID_WORK_PHONE"/>
			<xsd:enumeration value="RESERVED_PASSWORD"/>        
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ArrayOfValidationErrorsEnum">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="ValidationErrorsEnum" nillable="true" type="types:ValidationErrorsEnum"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="CreateAccountReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="acceptedPrivicyPolicyVersion" nillable="false" type="xsd:int"/>
              <xsd:element name="acceptedTermsAndConditionsVersion" nillable="false" type="xsd:int"/>
              <xsd:element name="accountType" nillable="false" type="types:AccountTypeEnum"/>
              <xsd:element name="address1" nillable="false" type="xsd:string"/>
              <xsd:element name="address2" nillable="true" type="xsd:string"/>
              <xsd:element name="address3" nillable="true" type="xsd:string"/>
              <xsd:element name="answer1" nillable="false" type="xsd:string"/>
              <xsd:element name="answer2" nillable="false" type="xsd:string"/>
              <xsd:element name="browser" nillable="true" type="xsd:string"/>
              <xsd:element name="countryOfResidence" nillable="true" type="xsd:string"/>
              <xsd:element name="countyState" nillable="true" type="xsd:string"/>
              <xsd:element name="currency" nillable="true" type="xsd:string"/>
              <xsd:element name="dateOfBirth" nillable="false" type="xsd:dateTime"/>
              <xsd:element name="depositLimit" nillable="false" type="xsd:double"/>
              <xsd:element name="depositLimitFrequency" nillable="false" type="types:GamcareLimitFreqEnum"/>
              <xsd:element name="emailAddress" nillable="false" type="xsd:string"/>
              <xsd:element name="firstName" nillable="false" type="xsd:string"/>
              <xsd:element name="gender" nillable="false" type="types:GenderEnum"/>
              <xsd:element name="homeTelephone" nillable="false" type="xsd:string"/>
              <xsd:element name="informProductsServices" nillable="false" type="xsd:boolean"/>
              <xsd:element name="informSpecialOffers" nillable="false" type="xsd:boolean"/>
              <xsd:element name="ipAddress" nillable="false" type="xsd:string"/>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
              <xsd:element name="lossLimit" nillable="false" type="xsd:double"/>              
              <xsd:element name="lossLimitFrequency" nillable="false" type="types:GamcareLimitFreqEnum"/>
              <xsd:element name="manualAddress" nillable="false" type="xsd:boolean"/>
              <xsd:element name="mobileTelephone" nillable="false" type="xsd:string"/>
              <xsd:element name="partnerId" nillable="false" type="xsd:int"/>
              <xsd:element name="password" nillable="true" type="xsd:string"/>
              <xsd:element name="postCode" nillable="true" type="xsd:string"/>
              <xsd:element name="preferredName" nillable="true" type="xsd:string"/>              
              <xsd:element name="productId" nillable="false" type="xsd:int"/>
              <xsd:element name="question1" nillable="false" type="types:SecurityQuestion1Enum"/>
              <xsd:element name="question2" nillable="false" type="types:SecurityQuestion2Enum"/>
              <xsd:element name="referrerCode" nillable="true" type="xsd:string"/>
              <xsd:element name="region" type="types:RegionEnum"/>
              <xsd:element name="subPartnerId" nillable="false" type="xsd:int"/>
              <xsd:element name="superPartnerId" nillable="false" type="xsd:int"/>
              <xsd:element name="surname" nillable="false" type="xsd:string"/>
              <xsd:element name="timeZone" nillable="true" type="xsd:string"/>
              <xsd:element name="title" nillable="false" type="types:TitleEnum"/>
              <xsd:element name="townCity" nillable="false" type="xsd:string"/>
              <xsd:element name="username" nillable="true" type="xsd:string"/>
              <xsd:element name="workTelephone" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="AccountTypeEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="STANDARD"/>
          <xsd:enumeration value="MARGIN"/>
          <xsd:enumeration value="TRADING"/>
          <xsd:enumeration value="AGENT_CLIENT"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:simpleType name="GamcareLimitFreqEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="DAILY"/>
          <xsd:enumeration value="WEEKLY"/>
		  <xsd:enumeration value="MONTHLY"/>
          <xsd:enumeration value="YEARLY"/>          
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:simpleType name="GenderEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="M"/>
          <xsd:enumeration value="F"/>
          <xsd:enumeration value="UNKNOWN"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:simpleType name="SecurityQuestion1Enum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="SQ1A"/>
          <xsd:enumeration value="SQ1B"/>
          <xsd:enumeration value="SQ1C"/>
          <xsd:enumeration value="SQ1D"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:simpleType name="SecurityQuestion2Enum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="SQ2A"/>
          <xsd:enumeration value="SQ2B"/>
          <xsd:enumeration value="SQ2C"/>
          <xsd:enumeration value="SQ2D"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:simpleType name="RegionEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="ZAF"/>
          <xsd:enumeration value="NA"/>
          <xsd:enumeration value="NORD"/>
          <xsd:enumeration value="GBR"/>
          <xsd:enumeration value="IRL"/>
          <xsd:enumeration value="AUS_NZL"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:simpleType name="TitleEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="Dr"/>
          <xsd:enumeration value="Mr"/>
          <xsd:enumeration value="Miss"/>
          <xsd:enumeration value="Mrs"/>
          <xsd:enumeration value="Ms"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:simpleType name="KYCStatusEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="DEFAULT"/>
          <xsd:enumeration value="AGE_VERIFIED"/>
		  <xsd:enumeration value="KYC"/>
          <xsd:enumeration value="KYC_NON_AUS"/>          
        </xsd:restriction>
      </xsd:simpleType>

		<xsd:simpleType name="ForgotPasswordErrorEnum">
			<xsd:restriction base="xsd:string">
	            <xsd:enumeration value="OK"/>
				<xsd:enumeration value="INVALID_USERNAME"/>
				<xsd:enumeration value="INVALID_COUNTRY_OF_RESIDENCE"/>
				<xsd:enumeration value="INVALID_EMAIL"/>
				<xsd:enumeration value="INVALID_ANSWER"/>
				<xsd:enumeration value="INVALID_PASSWORD"/>
				<xsd:enumeration value="TOO_MANY_ATTEMPTS_ACCOUNT_SUSPENDED"/>
				<xsd:enumeration value="API_ERROR"/>				
			</xsd:restriction>
		</xsd:simpleType>	  
		<xsd:simpleType name="ModifyPasswordErrorEnum">
			<xsd:restriction base="xsd:string">
	            <xsd:enumeration value="OK"/>
				<xsd:enumeration value="INVALID_PASSWORD"/>
				<xsd:enumeration value="INVALID_NEW_PASSWORD"/>
				<xsd:enumeration value="PASSWORDS_DONT_MATCH"/>
				<xsd:enumeration value="API_ERROR"/>				
			</xsd:restriction>
		</xsd:simpleType>	  
		<xsd:simpleType name="SetChatNameErrorEnum">
			<xsd:restriction base="xsd:string">
	            <xsd:enumeration value="OK"/>
				<xsd:enumeration value="INVALID_PASSWORD"/>
				<xsd:enumeration value="ACCOUNT_SUSPENDED"/>
				<xsd:enumeration value="ACCOUNT_NOT_FUNDED"/>
				<xsd:enumeration value="CHAT_NAME_UNAVAILABLE"/>
				<xsd:enumeration value="CANNOT_CHANGE_CHAT_NAME"/>
				<xsd:enumeration value="API_ERROR"/>				
			</xsd:restriction>
		</xsd:simpleType>	  
		<xsd:complexType name="ForgotPasswordReq">
			<xsd:complexContent>
			  <xsd:extension base="types:APIRequest">
				<xsd:sequence>
					<xsd:element name="username" type="xsd:string" nillable="false"/>
					<xsd:element name="emailAddress" type="xsd:string" nillable="false"/>
					<xsd:element name="countryOfResidence" type="xsd:string" nillable="false"/>
					<xsd:element name="forgottenPasswordAnswer1" type="xsd:string" nillable="true"/>
					<xsd:element name="forgottenPasswordAnswer2" type="xsd:string" nillable="true"/>
					<xsd:element name="newPassword" type="xsd:string" nillable="true"/>
					<xsd:element name="newPasswordRepeat" type="xsd:string" nillable="true"/>
				</xsd:sequence>
			  </xsd:extension>
			</xsd:complexContent>
		</xsd:complexType>
		<xsd:complexType name="ForgotPasswordResp">
			<xsd:complexContent>
				<xsd:extension base="types:APIResponse">
					<xsd:sequence>
						<xsd:element name="errorCode" type="types:ForgotPasswordErrorEnum"/>
						<xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
						<xsd:element name="question1" type="xsd:string" nillable="true"/>
						<xsd:element name="question2" type="xsd:string" nillable="true"/>
					</xsd:sequence>
				</xsd:extension>
			</xsd:complexContent>
		</xsd:complexType>	  
		<xsd:complexType name="ModifyPasswordReq">
			<xsd:complexContent>
			  <xsd:extension base="types:APIRequest">
				<xsd:sequence>
					<xsd:element name="password" type="xsd:string" nillable="false"/>
					<xsd:element name="newPassword" type="xsd:string" nillable="false"/>
					<xsd:element name="newPasswordRepeat" type="xsd:string" nillable="false"/>
				</xsd:sequence>
			  </xsd:extension>
			</xsd:complexContent>
		</xsd:complexType>
		<xsd:complexType name="ModifyPasswordResp">
			<xsd:complexContent>
				<xsd:extension base="types:APIResponse">
					<xsd:sequence>
						<xsd:element name="errorCode" type="types:ModifyPasswordErrorEnum"/>
						<xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
					</xsd:sequence>
				</xsd:extension>
			</xsd:complexContent>
		</xsd:complexType>	 
		<xsd:complexType name="SetChatNameReq">
			<xsd:complexContent>
			  <xsd:extension base="types:APIRequest">
				<xsd:sequence>
					<xsd:element name="password" type="xsd:string" nillable="false"/>
					<xsd:element name="chatName" type="xsd:string" nillable="false"/>
				</xsd:sequence>
			  </xsd:extension>
			</xsd:complexContent>
		</xsd:complexType>
		<xsd:complexType name="SetChatNameResp">
			<xsd:complexContent>
				<xsd:extension base="types:APIResponse">
					<xsd:sequence>
						<xsd:element name="errorCode" type="types:SetChatNameErrorEnum"/>
						<xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
					</xsd:sequence>
				</xsd:extension>
			</xsd:complexContent>
		</xsd:complexType>
    </xsd:schema>
    
    <xsd:schema elementFormDefault="qualified" targetNamespace="http://www.betfair.com/publicapi/v3/BFGlobalService/">
      <xsd:import namespace="http://www.betfair.com/publicapi/types/global/v3/"/>
      <xsd:element name="login">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:LoginReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="loginResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:LoginResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      
      <xsd:element name="retrieveLIMBMessage">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:RetrieveLIMBMessageReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="retrieveLIMBMessageResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:RetrieveLIMBMessageResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="submitLIMBMessage">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:SubmitLIMBMessageReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="submitLIMBMessageResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:SubmitLIMBMessageResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="logout">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:LogoutReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="logoutResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="false" type="types:LogoutResp"/> 
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

     <xsd:element name="keepAlive">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:KeepAliveReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="keepAliveResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:KeepAliveResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getEvents">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetEventsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getEventsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetEventsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getActiveEventTypes">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetEventTypesReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getActiveEventTypesResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetEventTypesResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getAllEventTypes">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetEventTypesReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getAllEventTypesResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetEventTypesResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getSubscriptionInfo">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetSubscriptionInfoReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getSubscriptionInfoResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetSubscriptionInfoResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>


      <xsd:element name="depositFromPaymentCard">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:DepositFromPaymentCardReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="depositFromPaymentCardResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:DepositFromPaymentCardResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="addPaymentCard">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:AddPaymentCardReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="addPaymentCardResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:AddPaymentCardResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="deletePaymentCard">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:DeletePaymentCardReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="deletePaymentCardResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:DeletePaymentCardResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="updatePaymentCard">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:UpdatePaymentCardReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="updatePaymentCardResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:UpdatePaymentCardResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getPaymentCard">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetPaymentCardReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getPaymentCardResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetPaymentCardResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="withdrawToPaymentCard">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:WithdrawToPaymentCardReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="withdrawToPaymentCardResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:WithdrawToPaymentCardResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="selfExclude">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:SelfExcludeReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="selfExcludeResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:SelfExcludeResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="convertCurrency">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:ConvertCurrencyReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="convertCurrencyResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:ConvertCurrencyResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getAllCurrencies">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetCurrenciesReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getAllCurrenciesResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetCurrenciesResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getAllCurrenciesV2">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetCurrenciesV2Req"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getAllCurrenciesV2Response">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetCurrenciesV2Resp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="viewReferAndEarn">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:ViewReferAndEarnReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="viewReferAndEarnResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:ViewReferAndEarnResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="viewProfile">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:ViewProfileReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="viewProfileResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:ViewProfileResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="viewProfileV2">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:ViewProfileV2Req"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="viewProfileV2Response">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:ViewProfileV2Resp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      
            <xsd:element name="modifyProfile">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:ModifyProfileReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="modifyProfileResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:ModifyProfileResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="createAccount">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:CreateAccountReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="createAccountResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:CreateAccountResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
		<xsd:element name="forgotPassword">
			<xsd:complexType>
				<xsd:sequence>
					<xsd:element name="request" type="types:ForgotPasswordReq"/>
				</xsd:sequence>
			</xsd:complexType>
		</xsd:element>
		<xsd:element name="forgotPasswordResponse">
			<xsd:complexType>
				<xsd:sequence>
					<xsd:element name="Result" nillable="true" type="types:ForgotPasswordResp"/>
				</xsd:sequence>
			</xsd:complexType>
		</xsd:element>
		<xsd:element name="modifyPassword">
			<xsd:complexType>
				<xsd:sequence>
					<xsd:element name="request" type="types:ModifyPasswordReq"/>
				</xsd:sequence>
			</xsd:complexType>
		</xsd:element>
		<xsd:element name="modifyPasswordResponse">
			<xsd:complexType>
				<xsd:sequence>
					<xsd:element name="Result" nillable="true" type="types:ModifyPasswordResp"/>
				</xsd:sequence>
			</xsd:complexType>
		</xsd:element>
		<xsd:element name="setChatName">
			<xsd:complexType>
				<xsd:sequence>
					<xsd:element name="request" type="types:SetChatNameReq"/>
				</xsd:sequence>
			</xsd:complexType>
		</xsd:element>
		<xsd:element name="setChatNameResponse">
			<xsd:complexType>
				<xsd:sequence>
					<xsd:element name="Result" nillable="true" type="types:SetChatNameResp"/>
				</xsd:sequence>
			</xsd:complexType>
		</xsd:element>

     	<xsd:element name="transferFunds">
			<xsd:complexType>
				<xsd:sequence>
					<xsd:element name="request" type="types:TransferFundsReq" />
				</xsd:sequence>
			</xsd:complexType>
		</xsd:element>
		<xsd:element name="transferFundsResponse">
			<xsd:complexType>
				<xsd:sequence>
					<xsd:element name="Result" nillable="true" type="types:TransferFundsResp" />
				</xsd:sequence>
			</xsd:complexType>
		</xsd:element>

    </xsd:schema>
 
  </wsdl:types>
  <wsdl:message name="loginIn">
    <wsdl:part element="tns:login" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="loginOut">
    <wsdl:part element="tns:loginResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="retrieveLIMBMessageIn">
    <wsdl:part element="tns:retrieveLIMBMessage" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="retrieveLIMBMessageOut">
    <wsdl:part element="tns:retrieveLIMBMessageResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="submitLIMBMessageIn">
    <wsdl:part element="tns:submitLIMBMessage" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="submitLIMBMessageOut">
    <wsdl:part element="tns:submitLIMBMessageResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="logoutIn">
    <wsdl:part element="tns:logout" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="logoutOut">
    <wsdl:part element="tns:logoutResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="keepAliveIn">
    <wsdl:part element="tns:keepAlive" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="keepAliveOut">
    <wsdl:part element="tns:keepAliveResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getEventsIn">
    <wsdl:part element="tns:getEvents" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getEventsOut">
    <wsdl:part element="tns:getEventsResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getActiveEventTypesIn">
    <wsdl:part element="tns:getActiveEventTypes" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getActiveEventTypesOut">
    <wsdl:part element="tns:getActiveEventTypesResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getAllEventTypesIn">
    <wsdl:part element="tns:getAllEventTypes" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getAllEventTypesOut">
    <wsdl:part element="tns:getAllEventTypesResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getSubscriptionInfoIn">
    <wsdl:part element="tns:getSubscriptionInfo" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getSubscriptionInfoOut">
    <wsdl:part element="tns:getSubscriptionInfoResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="depositFromPaymentCardIn">
    <wsdl:part element="tns:depositFromPaymentCard" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="depositFromPaymentCardOut">
    <wsdl:part element="tns:depositFromPaymentCardResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="addPaymentCardIn">
    <wsdl:part element="tns:addPaymentCard" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="addPaymentCardOut">
    <wsdl:part element="tns:addPaymentCardResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="deletePaymentCardIn">
    <wsdl:part element="tns:deletePaymentCard" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="deletePaymentCardOut">
    <wsdl:part element="tns:deletePaymentCardResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="updatePaymentCardIn">
    <wsdl:part element="tns:updatePaymentCard" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="updatePaymentCardOut">
    <wsdl:part element="tns:updatePaymentCardResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getPaymentCardIn">
    <wsdl:part element="tns:getPaymentCard" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getPaymentCardOut">
    <wsdl:part element="tns:getPaymentCardResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="withdrawToPaymentCardIn">
    <wsdl:part element="tns:withdrawToPaymentCard" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="withdrawToPaymentCardOut">
    <wsdl:part element="tns:withdrawToPaymentCardResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="selfExcludeIn">
    <wsdl:part element="tns:selfExclude" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="selfExcludeOut">
    <wsdl:part element="tns:selfExcludeResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="convertCurrencyIn">
    <wsdl:part element="tns:convertCurrency" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="convertCurrencyOut">
    <wsdl:part element="tns:convertCurrencyResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getAllCurrenciesIn">
    <wsdl:part element="tns:getAllCurrencies" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getAllCurrenciesOut">
    <wsdl:part element="tns:getAllCurrenciesResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getAllCurrenciesV2In">
    <wsdl:part element="tns:getAllCurrenciesV2" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getAllCurrenciesV2Out">
    <wsdl:part element="tns:getAllCurrenciesV2Response" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="viewReferAndEarnIn">
    <wsdl:part element="tns:viewReferAndEarn" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="viewReferAndEarnOut">
    <wsdl:part element="tns:viewReferAndEarnResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="viewProfileIn">
    <wsdl:part element="tns:viewProfile" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="viewProfileOut">
    <wsdl:part element="tns:viewProfileResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="viewProfileV2In">
    <wsdl:part element="tns:viewProfileV2" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="viewProfileV2Out">
    <wsdl:part element="tns:viewProfileV2Response" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="modifyProfileIn">
    <wsdl:part element="tns:modifyProfile" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="modifyProfileOut">
    <wsdl:part element="tns:modifyProfileResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="createAccountIn">
    <wsdl:part element="tns:createAccount" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="createAccountOut">
    <wsdl:part element="tns:createAccountResponse" name="parameters"/>
  </wsdl:message>
	<wsdl:message name="forgotPasswordIn">
		<wsdl:part name="parameters" element="tns:forgotPassword"/>
	</wsdl:message>
	<wsdl:message name="forgotPasswordOut">
		<wsdl:part name="parameters" element="tns:forgotPasswordResponse"/>
	</wsdl:message>
	<wsdl:message name="modifyPasswordIn">
		<wsdl:part name="parameters" element="tns:modifyPassword"/>
	</wsdl:message>
	<wsdl:message name="modifyPasswordOut">
		<wsdl:part name="parameters" element="tns:modifyPasswordResponse"/>
	</wsdl:message>
	<wsdl:message name="setChatNameIn">
		<wsdl:part name="parameters" element="tns:setChatName"/>
	</wsdl:message>
	<wsdl:message name="setChatNameOut">
		<wsdl:part name="parameters" element="tns:setChatNameResponse"/>
	</wsdl:message>

	<wsdl:message name="transferFundsIn">
		<wsdl:part name="parameters" element="tns:transferFunds"/>
	</wsdl:message>
	<wsdl:message name="transferFundsOut">
		<wsdl:part name="parameters" element="tns:transferFundsResponse"/>
	</wsdl:message>

  <wsdl:portType name="BFGlobalService">
    <wsdl:operation name="login">
      <wsdl:input message="tns:loginIn" name="loginIn"/>
      <wsdl:output message="tns:loginOut" name="loginOut"/>
    </wsdl:operation>
    
    <wsdl:operation name="retrieveLIMBMessage">
      <wsdl:input message="tns:retrieveLIMBMessageIn" name="retrieveLIMBMessageIn"/>
      <wsdl:output message="tns:retrieveLIMBMessageOut" name="retrieveLIMBMessageOut"/>
    </wsdl:operation>

    <wsdl:operation name="submitLIMBMessage">
      <wsdl:input message="tns:submitLIMBMessageIn" name="submitLIMBMessageIn"/>
      <wsdl:output message="tns:submitLIMBMessageOut" name="submitLIMBMessageOut"/>
    </wsdl:operation>

    <wsdl:operation name="logout">
      <wsdl:input message="tns:logoutIn" name="logoutIn"/>
      <wsdl:output message="tns:logoutOut" name="logoutOut"/>
    </wsdl:operation>

    <wsdl:operation name="keepAlive">
      <wsdl:input message="tns:keepAliveIn" name="keepAliveIn"/>
      <wsdl:output message="tns:keepAliveOut" name="keepAliveOut"/>
    </wsdl:operation>

    <wsdl:operation name="getEvents">
      <wsdl:input message="tns:getEventsIn" name="getEventsIn"/>
      <wsdl:output message="tns:getEventsOut" name="getEventsOut"/>
    </wsdl:operation>
    <wsdl:operation name="getActiveEventTypes">
      <wsdl:input message="tns:getActiveEventTypesIn" name="getActiveEventTypesIn"/>
      <wsdl:output message="tns:getActiveEventTypesOut" name="getActiveEventTypesOut"/>
    </wsdl:operation>
    <wsdl:operation name="getAllEventTypes">
      <wsdl:input message="tns:getAllEventTypesIn" name="getAllEventTypesIn"/>
      <wsdl:output message="tns:getAllEventTypesOut" name="getAllEventTypesOut"/>
    </wsdl:operation>

    <wsdl:operation name="getSubscriptionInfo">
      <wsdl:input message="tns:getSubscriptionInfoIn" name="getSubscriptionInfoIn"/>
      <wsdl:output message="tns:getSubscriptionInfoOut" name="getSubscriptionInfoOut"/>
    </wsdl:operation>

    <wsdl:operation name="depositFromPaymentCard">
      <wsdl:input message="tns:depositFromPaymentCardIn" name="depositFromPaymentCardIn"/>
      <wsdl:output message="tns:depositFromPaymentCardOut" name="depositFromPaymentCardOut"/>
    </wsdl:operation>

    <wsdl:operation name="addPaymentCard">
      <wsdl:input message="tns:addPaymentCardIn" name="addPaymentCardIn"/>
      <wsdl:output message="tns:addPaymentCardOut" name="addPaymentCardOut"/>
    </wsdl:operation>

    <wsdl:operation name="deletePaymentCard">
      <wsdl:input message="tns:deletePaymentCardIn" name="deletePaymentCardIn"/>
      <wsdl:output message="tns:deletePaymentCardOut" name="deletePaymentCardOut"/>
    </wsdl:operation>

    <wsdl:operation name="updatePaymentCard">
      <wsdl:input message="tns:updatePaymentCardIn" name="updatePaymentCardIn"/>
      <wsdl:output message="tns:updatePaymentCardOut" name="updatePaymentCardOut"/>
    </wsdl:operation>

    <wsdl:operation name="getPaymentCard">
      <wsdl:input message="tns:getPaymentCardIn" name="getPaymentCardIn"/>
      <wsdl:output message="tns:getPaymentCardOut" name="getPaymentCardOut"/>
    </wsdl:operation>

    <wsdl:operation name="withdrawToPaymentCard">
      <wsdl:input message="tns:withdrawToPaymentCardIn" name="withdrawToPaymentCardIn"/>
      <wsdl:output message="tns:withdrawToPaymentCardOut" name="withdrawToPaymentCardOut"/>
    </wsdl:operation>

    <wsdl:operation name="selfExclude">
      <wsdl:input message="tns:selfExcludeIn" name="selfExcludeIn"/>
      <wsdl:output message="tns:selfExcludeOut" name="selfExcludeOut"/>
    </wsdl:operation>

    <wsdl:operation name="convertCurrency">
      <wsdl:input message="tns:convertCurrencyIn" name="convertCurrencyIn"/>
      <wsdl:output message="tns:convertCurrencyOut" name="convertCurrencyOut"/>
    </wsdl:operation>
    <wsdl:operation name="getAllCurrencies">
      <wsdl:input message="tns:getAllCurrenciesIn" name="getAllCurrenciesIn"/>
      <wsdl:output message="tns:getAllCurrenciesOut" name="getAllCurrenciesOut"/>
    </wsdl:operation>
    <wsdl:operation name="getAllCurrenciesV2">
      <wsdl:input message="tns:getAllCurrenciesV2In" name="getAllCurrenciesV2In"/>
      <wsdl:output message="tns:getAllCurrenciesV2Out" name="getAllCurrenciesV2Out"/>
    </wsdl:operation>
    <wsdl:operation name="viewReferAndEarn">
      <wsdl:input message="tns:viewReferAndEarnIn" name="viewReferAndEarnIn"/>
      <wsdl:output message="tns:viewReferAndEarnOut" name="viewReferAndEarnOut"/>
    </wsdl:operation>
    <wsdl:operation name="viewProfile">
      <wsdl:input message="tns:viewProfileIn" name="viewProfileIn"/>
      <wsdl:output message="tns:viewProfileOut" name="viewProfileOut"/>
    </wsdl:operation>

    <wsdl:operation name="viewProfileV2">
      <wsdl:input message="tns:viewProfileV2In" name="viewProfileV2In"/>
      <wsdl:output message="tns:viewProfileV2Out" name="viewProfileV2Out"/>
    </wsdl:operation>

    <wsdl:operation name="modifyProfile">
      <wsdl:input message="tns:modifyProfileIn" name="modifyProfileIn"/>
      <wsdl:output message="tns:modifyProfileOut" name="modifyProfileOut"/>
    </wsdl:operation>

    <wsdl:operation name="createAccount">
      <wsdl:input message="tns:createAccountIn" name="createAccountIn"/>
      <wsdl:output message="tns:createAccountOut" name="createAccountOut"/>
    </wsdl:operation>
	<wsdl:operation name="forgotPassword">
		<wsdl:input name="forgotPasswordIn" message="tns:forgotPasswordIn"/>
		<wsdl:output name="forgotPasswordOut" message="tns:forgotPasswordOut"/>
	</wsdl:operation>
	<wsdl:operation name="modifyPassword">
		<wsdl:input name="modifyPasswordIn" message="tns:modifyPasswordIn"/>
		<wsdl:output name="modifyPasswordOut" message="tns:modifyPasswordOut"/>
	</wsdl:operation>
	<wsdl:operation name="setChatName">
		<wsdl:input name="setChatNameIn" message="tns:setChatNameIn"/>
		<wsdl:output name="setChatNameOut" message="tns:setChatNameOut"/>
	</wsdl:operation>

	<wsdl:operation name="transferFunds">
		<wsdl:input name="transferFundsIn" message="tns:transferFundsIn" />
		<wsdl:output name="transferFundsOut" message="tns:transferFundsOut" />
	</wsdl:operation>
  </wsdl:portType>
  <wsdl:binding name="BFGlobalService" type="tns:BFGlobalService">
    <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
    
    <wsdl:operation name="login">
      <soap:operation soapAction="login" style="document"/>
      <wsdl:input name="loginIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="loginOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    
    <wsdl:operation name="retrieveLIMBMessage">
      <soap:operation soapAction="retrieveLIMBMessage" style="document"/>
      <wsdl:input name="retrieveLIMBMessageIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="retrieveLIMBMessageOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="submitLIMBMessage">
      <soap:operation soapAction="submitLIMBMessage" style="document"/>
      <wsdl:input name="submitLIMBMessageIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="submitLIMBMessageOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="logout">
      <soap:operation soapAction="logout" style="document"/>
      <wsdl:input name="logoutIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="logoutOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="keepAlive">
      <soap:operation soapAction="keepAlive" style="document"/>
      <wsdl:input name="keepAliveIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="keepAliveOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="getEvents">
      <soap:operation soapAction="getEvents" style="document"/>
      <wsdl:input name="getEventsIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getEventsOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getActiveEventTypes">
      <soap:operation soapAction="getActiveEventTypes" style="document"/>
      <wsdl:input name="getActiveEventTypesIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getActiveEventTypesOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getAllEventTypes">
      <soap:operation soapAction="getAllEventTypes" style="document"/>
      <wsdl:input name="getAllEventTypesIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getAllEventTypesOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="getSubscriptionInfo">
      <soap:operation soapAction="getSubscriptionInfo" style="document"/>
      <wsdl:input name="getSubscriptionInfoIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getSubscriptionInfoOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="depositFromPaymentCard">
      <soap:operation soapAction="depositFromPaymentCard" style="document"/>
      <wsdl:input name="depositFromPaymentCardIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="depositFromPaymentCardOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="addPaymentCard">
      <soap:operation soapAction="addPaymentCard" style="document"/>
      <wsdl:input name="addPaymentCardIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="addPaymentCardOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="deletePaymentCard">
      <soap:operation soapAction="deletePaymentCard" style="document"/>
      <wsdl:input name="deletePaymentCardIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="deletePaymentCardOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="updatePaymentCard">
      <soap:operation soapAction="updatePaymentCard" style="document"/>
      <wsdl:input name="updatePaymentCardIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="updatePaymentCardOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="getPaymentCard">
      <soap:operation soapAction="getPaymentCard" style="document"/>
      <wsdl:input name="getPaymentCardIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getPaymentCardOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="withdrawToPaymentCard">
      <soap:operation soapAction="withdrawToPaymentCard" style="document"/>
      <wsdl:input name="withdrawToPaymentCardIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="withdrawToPaymentCardOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="selfExclude">
      <soap:operation soapAction="selfExclude" style="document"/>
      <wsdl:input name="selfExcludeIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="selfExcludeOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="convertCurrency">
      <soap:operation soapAction="convertCurrency" style="document"/>
      <wsdl:input name="convertCurrencyIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="convertCurrencyOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getAllCurrencies">
      <soap:operation soapAction="getAllCurrencies" style="document"/>
      <wsdl:input name="getAllCurrenciesIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getAllCurrenciesOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="getAllCurrenciesV2">
      <soap:operation soapAction="getAllCurrenciesV2" style="document"/>
      <wsdl:input name="getAllCurrenciesV2In">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getAllCurrenciesV2Out">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="viewReferAndEarn">
      <soap:operation soapAction="viewReferAndEarn" style="document"/>
      <wsdl:input name="viewReferAndEarnIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="viewReferAndEarnOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="viewProfile">
      <soap:operation soapAction="viewProfile" style="document"/>
      <wsdl:input name="viewProfileIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="viewProfileOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="viewProfileV2">
      <soap:operation soapAction="viewProfileV2" style="document"/>
      <wsdl:input name="viewProfileV2In">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="viewProfileV2Out">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="modifyProfile">
      <soap:operation soapAction="modifyProfile" style="document"/>
      <wsdl:input name="modifyProfileIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="modifyProfileOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="createAccount">
      <soap:operation soapAction="createAccount" style="document"/>
      <wsdl:input name="createAccountIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="createAccountOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
	<wsdl:operation name="forgotPassword">
		<soap:operation soapAction="forgotPassword" style="document"/>
		<wsdl:input name="forgotPasswordIn">
			<soap:body use="literal"/>
		</wsdl:input>
		<wsdl:output name="forgotPasswordOut">
			<soap:body use="literal"/>
		</wsdl:output>
	</wsdl:operation>
	<wsdl:operation name="modifyPassword">
		<soap:operation soapAction="modifyPassword" style="document"/>
		<wsdl:input name="modifyPasswordIn">
			<soap:body use="literal"/>
		</wsdl:input>
		<wsdl:output name="modifyPasswordOut">
			<soap:body use="literal"/>
		</wsdl:output>
	</wsdl:operation>
	<wsdl:operation name="setChatName">
		<soap:operation soapAction="setChatName" style="document"/>
		<wsdl:input name="setChatNameIn">
			<soap:body use="literal"/>
		</wsdl:input>
		<wsdl:output name="setChatNameOut">
			<soap:body use="literal"/>
		</wsdl:output>
	</wsdl:operation>
	

	<wsdl:operation name="transferFunds">
		<soap:operation soapAction="transferFunds" style="document" />
		<wsdl:input name="transferFundsIn">
			<soap:body use="literal" />
		</wsdl:input>
		<wsdl:output name="transferFundsOut">
			<soap:body use="literal" />
		</wsdl:output>
	</wsdl:operation>
  </wsdl:binding>
  <wsdl:service name="BFGlobalService">
    <wsdl:port binding="tns:BFGlobalService" name="BFGlobalService">
      <soap:address location="https://api.betfair.com/global/v3/BFGlobalService"/>
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>
'''

BFExchangeService = '''
<?xml version="1.0" encoding="UTF-8"?>

<!--

Copyright 2003-2004 The Sporting Exchange Limited. All rights reserved. 
The presentation, distribution or other dissemination of the information contained herein by The Sporting Exchange Limited (Betfair) is not a license, either expressly or impliedly, to any intellectual property owned or controlled by Betfair.
Save as provided by statute and to the fullest extent permitted by law, the following provisions set out the entire liability of Betfair (including any liability for the acts and omissions of its employees, agents and sub-contractors) to the User in respect of the use of its WSDL file whether in contract, tort, statute, equity or otherwise: 
(a)     The User acknowledges and agrees that (except as expressly provided in this Agreement) the WSDL is provided "AS IS" without warranties of any kind (whether express or implied);
(b)    All conditions, warranties, terms and undertakings (whether express or implied, statutory or otherwise relating to the delivery, performance, quality, uninterrupted use, fitness for purpose, occurrence or reliability of the WSDL are hereby excluded to the fullest extent permitted by law; and 
(c)     Betfair shall not be liable to the User for loss of profit (whether direct or indirect), loss of contracts or goodwill, lost advertising, loss of data or any type of special, indirect, consequential or economic loss (including loss or damage suffered by the User as a result of an action brought by a third party) even if such loss was reasonably foreseeable or Betfair had been advised of the possibility of the User incurring such loss.
No exclusion or limitation set out in this Agreement shall apply in the case of fraud or fraudulent concealment, death or personal injury resulting from the negligence of either party or any of its employees, agents or sub-contractors; and/or any breach of the obligations implied by (as appropriate) section 12 of the Sale of Goods Act 1979, section 2 of the Supply of Goods and Services Act 1982 or section 8 of the Supply of Goods (Implied Terms) Act 1973.

-->

<wsdl:definitions name="BFExchangeService"
  targetNamespace="http://www.betfair.com/publicapi/v5/BFExchangeService/"
  xmlns:types="http://www.betfair.com/publicapi/types/exchange/v5/"
  xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
  xmlns:tns="http://www.betfair.com/publicapi/v5/BFExchangeService/"
  xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <wsdl:types>
    <xsd:schema targetNamespace="http://www.betfair.com/publicapi/types/exchange/v5/">
      <xsd:import namespace="http://schemas.xmlsoap.org/soap/encoding/"/>
      <xsd:complexType abstract="true" name="APIResponse">
        <xsd:sequence>
          <xsd:element name="header" nillable="true" type="types:APIResponseHeader"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="APIResponseHeader">
        <xsd:sequence>
          <xsd:element name="errorCode" type="types:APIErrorEnum"/>
          <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
          <xsd:element name="sessionToken" nillable="true" type="xsd:string"/>
          <xsd:element name="timestamp" type="xsd:dateTime"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="APIErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INTERNAL_ERROR"/>
          <xsd:enumeration value="EXCEEDED_THROTTLE"/>
          <xsd:enumeration value="USER_NOT_SUBSCRIBED_TO_PRODUCT"/>
          <xsd:enumeration value="SUBSCRIPTION_INACTIVE_OR_SUSPENDED"/>
          <xsd:enumeration value="VENDOR_SOFTWARE_INACTIVE"/>
          <xsd:enumeration value="VENDOR_SOFTWARE_INVALID"/>
          <xsd:enumeration value="SERVICE_NOT_AVAILABLE_IN_PRODUCT"/>
          <xsd:enumeration value="NO_SESSION"/>
          <xsd:enumeration value="TOO_MANY_REQUESTS"/>
          <xsd:enumeration value="PRODUCT_REQUIRES_FUNDED_ACCOUNT"/>
          <xsd:enumeration value="SERVICE_NOT_AVAILABLE_FOR_LOGIN_STATUS"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType abstract="true" name="APIRequest">
        <xsd:sequence>
          <xsd:element name="header" nillable="true" type="types:APIRequestHeader"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="APIRequestHeader">
        <xsd:sequence>
          <xsd:element name="clientStamp" type="xsd:long"/>
          <xsd:element name="sessionToken" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="GetAccountFundsResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="availBalance" nillable="false" type="xsd:double"/>
              <xsd:element name="balance" nillable="false" type="xsd:double"/>
              <xsd:element name="commissionRetain" nillable="false" type="xsd:double"/>
              <xsd:element name="creditLimit" nillable="false" type="xsd:double"/>
              <xsd:element name="currentBetfairPoints" nillable="false" type="xsd:int"/>
              <xsd:element name="expoLimit" nillable="false" type="xsd:double"/>
              <xsd:element name="exposure" nillable="false" type="xsd:double"/>
              <xsd:element name="holidaysAvailable" nillable="false" type="xsd:int"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="nextDiscount" nillable="false" type="xsd:double"/>
              <xsd:element name="withdrawBalance" nillable="false" type="xsd:double"/>
              <xsd:element name="errorCode" type="types:GetAccountFundsErrorEnum" />
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetAccountFundsErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="EXPOSURE_CALC_IN_PROGRESS"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="GetAccountFundsReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest"/>
        </xsd:complexContent>
      </xsd:complexType>
      
      <xsd:complexType name="GetSilksResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetSilksErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="marketDisplayDetails" nillable="true" type="types:ArrayOfMarketDisplayDetail"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="MarketDisplayDetail">
        <xsd:sequence>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="racingSilks" nillable="true" type="types:ArrayOfRacingSilk"/>
          <xsd:element name="errorCode" type="types:MarketDisplayErrorEnum"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfMarketDisplayDetail">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="MarketDisplayDetail" nillable="true" type="types:MarketDisplayDetail"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="RacingSilk">
        <xsd:sequence>
          <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
          <xsd:element name="silksURL" nillable="true" type="xsd:string"/>
          <xsd:element name="silksText" nillable="true" type="xsd:string"/>
          <xsd:element name="trainerName" nillable="true" type="xsd:string"/>
          <xsd:element name="ageWeight" nillable="true" type="xsd:string"/>
          <xsd:element name="form" nillable="true" type="xsd:string"/>
          <xsd:element name="daysSince" nillable="false" type="xsd:int"/>
          <xsd:element name="jockeyClaim" nillable="false" type="xsd:int"/>
          <xsd:element name="wearing" nillable="true" type="xsd:string"/>
          <xsd:element name="saddleCloth" nillable="false" type="xsd:int"/>
          <xsd:element name="stallDraw" nillable="false" type="xsd:int"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfRacingSilk">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="RacingSilk" nillable="true" type="types:RacingSilk"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="GetSilksErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_LOCALE"/>
          <xsd:enumeration value="INVALID_NUMBER_OF_MARKETS"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:simpleType name="MarketDisplayErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_MARKET"/>
          <xsd:enumeration value="NO_SILKS_AVAILABLE"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="GetSilksReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
              <xsd:element name="markets" nillable="true" type="types:ArrayOfInt"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      
      <xsd:complexType name="GetSilksV2Resp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetSilksErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="marketDisplayDetails" nillable="true" type="types:ArrayOfMarketDisplayDetailV2"/>
            </xsd:sequence>
          </xsd:extension>   
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="MarketDisplayDetailV2">
        <xsd:sequence>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="racingSilks" nillable="true" type="types:ArrayOfRacingSilkV2"/>
          <xsd:element name="errorCode" type="types:MarketDisplayErrorEnum"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfMarketDisplayDetailV2">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="MarketDisplayDetail" nillable="true" type="types:MarketDisplayDetailV2"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="Breeding">
        <xsd:sequence>
          <xsd:element name="name" nillable="true" type="xsd:string"/>
          <xsd:element name="bred" nillable="true" type="xsd:string"/>
          <xsd:element name="yearBorn" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="RacingSilkV2">
        <xsd:complexContent>
            <xsd:extension base="types:RacingSilk">
              <xsd:sequence>
                <!-- Version 2 fields -->
                <xsd:element name="ownerName" nillable="true" type="xsd:string"/>
                <xsd:element name="jockeyName" nillable="true" type="xsd:string"/>
                <xsd:element name="colour" nillable="true" type="xsd:string"/>
                <xsd:element name="sex" nillable="true" type="xsd:string"/>
                <xsd:element name="bred" nillable="true" type="xsd:string"/>
                <xsd:element name="forecastPriceNumerator" nillable="false" type="xsd:int"/>
                <xsd:element name="forecastPriceDenominator" nillable="false" type="xsd:int"/>
                <xsd:element name="officialRating" nillable="false" type="xsd:int"/>
                <xsd:element name="sire" nillable="true" type="types:Breeding"/>
                <xsd:element name="dam" nillable="true" type="types:Breeding"/>
                <xsd:element name="damSire" nillable="true" type="types:Breeding"/>
              </xsd:sequence>
            </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfRacingSilkV2">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="RacingSilk" nillable="true" type="types:RacingSilkV2"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetSilksV2Req">
        <xsd:complexContent>
          <xsd:extension base="types:GetSilksReq">
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      
      <xsd:complexType name="CancelBetsResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="betResults" nillable="true" type="types:ArrayOfCancelBetsResult"/>
              <xsd:element name="errorCode" type="types:CancelBetsErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="CancelBetsResult">
        <xsd:sequence>
          <xsd:element name="betId" type="xsd:long"/>
          <xsd:element name="resultCode" type="types:CancelBetsResultEnum"/>
          <xsd:element name="sizeCancelled" nillable="false" type="xsd:double"/>
          <xsd:element name="sizeMatched" nillable="false" type="xsd:double"/>
          <xsd:element name="success" nillable="false" type="xsd:boolean"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="CancelBetsResultEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="BET_IN_PROGRESS"/>
          <xsd:enumeration value="BBM_DAEMON_NOT_AVAILABLE"/>
          <xsd:enumeration value="INVALID_BET_ID"/>
          <xsd:enumeration value="UNKNOWN_ERROR"/>
          <xsd:enumeration value="TAKEN_OR_LAPSED"/>
          <xsd:enumeration value="REMAINING_CANCELLED"/>
          <xsd:enumeration value="INPLAY_FORBIDDEN"/>
          <xsd:enumeration value="FROM_COUNTRY_FORBIDDEN"/>
          <xsd:enumeration value="INPLAY_FROM_COUNTRY_FORBIDDEN"/>
          <xsd:enumeration value="SITE_UPGRADE"/>
          <xsd:enumeration value="BET_NOT_CANCELLED"/>
          <xsd:enumeration value="BSP_BETS_CANNOT_BE_CANCELLED"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ArrayOfCancelBetsResult">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="CancelBetsResult" nillable="true" type="types:CancelBetsResult"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="CancelBetsErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="BET_IN_PROGRESS"/>
          <xsd:enumeration value="BBM_DAEMON_NOT_AVAILABLE"/>          
          <xsd:enumeration value="INVALID_NUMER_OF_CANCELLATIONS"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
          <xsd:enumeration value="MARKET_STATUS_INVALID"/>
          <xsd:enumeration value="MARKET_IDS_DONT_MATCH"/>
          <xsd:enumeration value="INVALID_MARKET_ID"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="CancelBetsReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="bets" nillable="true" type="types:ArrayOfCancelBets"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="CancelBets">
        <xsd:sequence>
          <xsd:element name="betId" type="xsd:long"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfCancelBets">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="CancelBets" nillable="true" type="types:CancelBets"/>
        </xsd:sequence>
      </xsd:complexType>
      
      
            <xsd:complexType name="CancelBetsByMarketReq">
              <xsd:complexContent>
                <xsd:extension base="types:APIRequest">
                  <xsd:sequence>
                    <xsd:element name="markets" nillable="true" type="types:ArrayOfInt"/>
                  </xsd:sequence>
                </xsd:extension>
              </xsd:complexContent>
            </xsd:complexType>
            <xsd:complexType name="CancelBetsByMarketResp">
              <xsd:complexContent>
                <xsd:extension base="types:APIResponse">
                  <xsd:sequence>
                    <xsd:element name="results" nillable="true" type="types:ArrayOfCancelBetsByMarketResult"/>
                    <xsd:element name="errorCode" type="types:CancelBetsByMarketErrorEnum"/>
                    <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
                  </xsd:sequence>
                </xsd:extension>
              </xsd:complexContent>
            </xsd:complexType>
            <xsd:simpleType name="CancelBetsByMarketErrorEnum">
              <xsd:restriction base="xsd:string">
                <xsd:enumeration value="OK"/>
                <xsd:enumeration value="INVALID_NUMBER_OF_MARKETS"/>
                <xsd:enumeration value="API_ERROR"/>
              </xsd:restriction>
            </xsd:simpleType>
            <xsd:complexType name="ArrayOfCancelBetsByMarketResult">
              <xsd:sequence>
                <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
                  name="CancelBetsByMarketResult" nillable="true" type="types:CancelBetsByMarketResult"/>
              </xsd:sequence>
            </xsd:complexType>
            <xsd:complexType name="CancelBetsByMarketResult">
              <xsd:sequence>
                <xsd:element name="marketId" type="xsd:int"/>
                <xsd:element name="resultCode" type="types:CancelBetsByMarketResultEnum"/>
              </xsd:sequence>
            </xsd:complexType>
            <xsd:simpleType name="CancelBetsByMarketResultEnum">
              <xsd:restriction base="xsd:string">
                <xsd:enumeration value="OK"/>
                <xsd:enumeration value="MARKET_STATUS_INVALID"/>
                <xsd:enumeration value="UNKNOWN_ERROR"/>
                <xsd:enumeration value="INVALID_MARKET"/>
                <xsd:enumeration value="NO_UNMATCHED_BETS"/>
                <xsd:enumeration value="INPLAY_FORBIDDEN"/>
                <xsd:enumeration value="FROM_COUNTRY_FORBIDDEN"/>
                <xsd:enumeration value="INPLAY_FROM_COUNTRY_FORBIDDEN"/>
                <xsd:enumeration value="SITE_UPGRADE"/>
                <xsd:enumeration value="BET_NOT_CANCELLED"/>
              </xsd:restriction>
      </xsd:simpleType>
      
      <xsd:complexType name="UpdateBetsResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="betResults" nillable="true" type="types:ArrayOfUpdateBetsResult"/>
              <xsd:element name="errorCode" type="types:UpdateBetsErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="UpdateBetsResult">
        <xsd:sequence>
          <xsd:element name="betId" nillable="false" type="xsd:long"/>
          <xsd:element name="newBetId" nillable="true" type="xsd:long"/>
          <xsd:element name="sizeCancelled" nillable="true" type="xsd:double"/>
          <xsd:element name="newSize" nillable="true" type="xsd:double"/>
          <xsd:element name="newPrice" nillable="true" type="xsd:double"/> 
          <xsd:element name="resultCode" type="types:UpdateBetsResultEnum"/>
          <xsd:element name="success" nillable="false" type="xsd:boolean"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="UpdateBetsResultEnum">
        <xsd:restriction base="xsd:string">
            <xsd:enumeration value="OK"/>
            <xsd:enumeration value="BET_IN_PROGRESS"/>
            <xsd:enumeration value="BBM_DAEMON_NOT_AVAILABLE"/>           
            <xsd:enumeration value="BET_CANCELLED_REMAINING_UNMATCHED"/>
            <xsd:enumeration value="BET_CANNOT_BE_ACCEPTED"/>
            <xsd:enumeration value="BET_NOT_CANCELLED"/>
            <xsd:enumeration value="BET_TAKEN_OR_LAPSED"/>
            <xsd:enumeration value="CANCELLED_NOT_PLACED"/>
            <xsd:enumeration value="ERROR_LINE_EXPO_BET_CANCELLED_NOT_PLACED"/>
            <xsd:enumeration value="EVENT_CLOSED_CANNOT_MODIFY_BET"/>
            <xsd:enumeration value="EXCEEDED_EXPOSURE_OR_AVAILABLE_TO_BET_BALANCE"/>
            <xsd:enumeration value="EXPOSURE_CALCULATION_ERROR"/>
            <xsd:enumeration value="EXPOSURE_CALCULATION_IN_PROGRESS"/>
            <xsd:enumeration value="FROM_COUNTRY_ON_EVENT_FORBIDDEN"/>
            <xsd:enumeration value="INPLAY_FROM_COUNTRY_FORBIDDEN"/>
            <xsd:enumeration value="INSUFFICIENT_BALANCE"/>
            <xsd:enumeration value="INVALID_BET_ID"/>
            <xsd:enumeration value="INVALID_OLD_PRICE"/>
            <xsd:enumeration value="INVALID_OLD_SIZE"/>
            <xsd:enumeration value="INVALID_PRICE"/>
            <xsd:enumeration value="INVALID_PRICE_AND_SIZE"/>
            <xsd:enumeration value="INVALID_SIZE"/>
            <xsd:enumeration value="LOSS_LIMIT_EXCEEDED"/>
            <xsd:enumeration value="NEW_BET_SUBMITTED_SUCCESSFULLY"/>
            <xsd:enumeration value="NOT_PLACED_EXPOSURE_EXCEEDED"/>
            <xsd:enumeration value="NOT_PLACED_REMAINING_CANCELLED"/>
            <xsd:enumeration value="OK_REMAINING_CANCELLED"/>
            <xsd:enumeration value="PARTIAL_CANCELLATION"/>
            <xsd:enumeration value="REMAINING_SIZE_CANCELLED"/>
            <xsd:enumeration value="RUNNER_REMOVED"/>
            <xsd:enumeration value="SITE_UPGRADE"/>
            <xsd:enumeration value="UNKNOWN_ERROR"/>
            <xsd:enumeration value="VACANT_TRAP"/>
            <xsd:enumeration value="WRONG_MININUM_PERMITTED_BET_SIZE"/>
            <xsd:enumeration value="BSP_BETS_CANNOT_BE_CANCELLED"/>
            <xsd:enumeration value="BSP_BETTING_NOT_ALLOWED"/>
            <xsd:enumeration value="BSP_BETTING_NOT_SUPPORTED"/>
            <xsd:enumeration value="BSP_INVALID_PRICE_LIMIT"/>
            <xsd:enumeration value="BSP_MOC_BETS_EDITING_NOT_PERMITTED"/>
            <xsd:enumeration value="INVALID_BSP_BET_UPDATE"/>
            <xsd:enumeration value="INVALID_INPUTS"/>
            <xsd:enumeration value="PERSISTENCE_MODIFICATION_SUCCESS"/>
            <xsd:enumeration value="INVALID_NEW_PRICE_LIMIT"/>
            <xsd:enumeration value="BSP_INVALID_PERSISTENCE"/>
		</xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ArrayOfUpdateBetsResult">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="UpdateBetsResult" nillable="true" type="types:UpdateBetsResult"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="UpdateBetsErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
		  <xsd:enumeration value="BET_IN_PROGRESS"/>
		  <xsd:enumeration value="BBM_DAEMON_NOT_AVAILABLE"/>          
          <xsd:enumeration value="ACCOUNT_PENDING"/>
          <xsd:enumeration value="ACCOUNT_SUSPENDED"/>
          <xsd:enumeration value="ACCOUNT_CLOSED"/>
          <xsd:enumeration value="INVALID_NUMBER_OF_BETS"/>
          <xsd:enumeration value="INVALID_MARKET_ID"/>
          <xsd:enumeration value="MARKET_STATUS_INVALID"/>
          <xsd:enumeration value="FROM_COUNTRY_FORBIDDEN"/>
          <xsd:enumeration value="API_ERROR"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="UpdateBetsReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="bets" nillable="true" type="types:ArrayOfUpdateBets"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="UpdateBets">
        <xsd:sequence>
          <xsd:element name="betId" type="xsd:long"/>
          <xsd:element name="newPrice" nillable="true" type="xsd:double"/>
          <xsd:element name="newSize" nillable="false" type="xsd:double"/>
          <xsd:element name="oldPrice" nillable="true" type="xsd:double"/>
          <xsd:element name="oldSize" nillable="false" type="xsd:double"/>
	  <xsd:element name="oldBetPersistenceType" type="types:BetPersistenceTypeEnum"/>          
	  <xsd:element name="newBetPersistenceType" type="types:BetPersistenceTypeEnum"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfUpdateBets">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="UpdateBets" nillable="true" type="types:UpdateBets"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="PlaceBetsResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="betResults" nillable="true" type="types:ArrayOfPlaceBetsResult"/>
              <xsd:element name="errorCode" type="types:PlaceBetsErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="PlaceBetsResult">
        <xsd:sequence>
          <xsd:element name="averagePriceMatched" nillable="false" type="xsd:double"/>
          <xsd:element name="betId" type="xsd:long"/>
          <xsd:element name="resultCode" type="types:PlaceBetsResultEnum"/>
          <xsd:element name="sizeMatched" nillable="false" type="xsd:double"/>
          <xsd:element name="success" nillable="false" type="xsd:boolean"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="PlaceBetsErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="BETWEEN_1_AND_60_BETS_REQUIRED"/>
          <xsd:enumeration value="EVENT_INACTIVE"/>
          <xsd:enumeration value="EVENT_CLOSED"/>
          <xsd:enumeration value="EVENT_SUSPENDED"/>
          <xsd:enumeration value="ACCOUNT_CLOSED"/>
          <xsd:enumeration value="ACCOUNT_SUSPENDED"/>
          <xsd:enumeration value="AUTHORISATION_PENDING"/>
          <xsd:enumeration value="INTERNAL_ERROR"/>
          <xsd:enumeration value="SITE_UPGRADE"/>
          <xsd:enumeration value="BACK_LAY_COMBINATION"/>
          <xsd:enumeration value="INVALID_MARKET"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
          <xsd:enumeration value="DIFFERING_MARKETS"/>
          <xsd:enumeration value="FROM_COUNTRY_FORBIDDEN"/>
          <xsd:enumeration value="ACCOUNT_IS_EXCLUDED"/>
          <xsd:enumeration value="BET_IN_PROGRESS"/>
          <xsd:enumeration value="BBM_DAEMON_NOT_AVAILABLE"/>         
          <xsd:enumeration value="BSP_BETTING_NOT_SUPPORTED"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:simpleType name="PlaceBetsResultEnum">
        <xsd:restriction base="xsd:string">
            <xsd:enumeration value="OK"/>
            <xsd:enumeration value="BET_IN_PROGRESS"/>
            <xsd:enumeration value="BBM_DAEMON_NOT_AVAILABLE"/>         
            <xsd:enumeration value="ACCOUNT_CLOSED"/>
            <xsd:enumeration value="ACCOUNT_IS_EXCLUDED"/>
            <xsd:enumeration value="ACCOUNT_SUSPENDED"/>
            <xsd:enumeration value="CANNOT_ACCEPT_BET"/>
            <xsd:enumeration value="EXPOSURE_CALCULATION_IN_PROGRESS"/>
            <xsd:enumeration value="EXPOSURE_OR_AVAILABLE_BALANCE_EXCEEDED"/>
            <xsd:enumeration value="FROM_COUNTRY_ON_EVENT_FORBIDDEN"/>
            <xsd:enumeration value="INPLAY_FROM_COUNTRY_FORBIDDEN"/>
            <xsd:enumeration value="INSUFFICIENT_BALANCE"/>
            <xsd:enumeration value="INVALID_ASIAN_LINE_ID"/>
            <xsd:enumeration value="INVALID_BET_TYPE"/>
            <xsd:enumeration value="INVALID_INCREMENT"/>
            <xsd:enumeration value="INVALID_MARKET"/>
            <xsd:enumeration value="INVALID_PRICE"/>
            <xsd:enumeration value="INVALID_SELECTION"/>
            <xsd:enumeration value="INVALID_SIZE"/>
            <xsd:enumeration value="LINES_OUT_OF_RANGE"/>
            <xsd:enumeration value="LOSS_LIMIT_EXCEEDED"/>
            <xsd:enumeration value="SELECTION_REMOVED"/>
            <xsd:enumeration value="UNKNOWN_ERROR"/>
            <xsd:enumeration value="VACANT_TRAP"/>      
            <xsd:enumeration value="EVENT_CLOSED"/>
            <xsd:enumeration value="AUTHORISATION_PENDING"/>
            <xsd:enumeration value="BSP_BETTING_NOT_ALLOWED"/>
            <xsd:enumeration value="BSP_BETTING_NOT_SUPPORTED"/>
            <xsd:enumeration value="BSP_MULTIPLE_BETS_NOT_ALLOWED"/>
            <xsd:enumeration value="EVENT_RECONCILED"/>
            <xsd:enumeration value="INVALID_PERSISTENCE"/>
            <xsd:enumeration value="ACCOUNT_LOCKED"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ArrayOfPlaceBetsResult">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="PlaceBetsResult" nillable="true" type="types:PlaceBetsResult"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="PlaceBetsReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="bets" nillable="true" type="types:ArrayOfPlaceBets"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="PlaceBets">
        <xsd:sequence>
          <xsd:element name="asianLineId" nillable="false" type="xsd:int"/>
          <xsd:element name="betType" type="types:BetTypeEnum"/>
          <xsd:element name="betCategoryType" type="types:BetCategoryTypeEnum"/>
          <xsd:element name="betPersistenceType" type="types:BetPersistenceTypeEnum"/>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="price" nillable="false" type="xsd:double"/>
          <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
          <xsd:element name="size" nillable="true" type="xsd:double"/>
          <xsd:element name="bspLiability" nillable="true" type="xsd:double"/>          
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="BetTypeEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="B"/>
          <xsd:enumeration value="L"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ArrayOfPlaceBets">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="PlaceBets" nillable="true" type="types:PlaceBets"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:simpleType name="MarketTypeEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="O"/>
          <xsd:enumeration value="L"/>
          <xsd:enumeration value="R"/>
          <xsd:enumeration value="A"/>
          <xsd:enumeration value="NOT_APPLICABLE"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:simpleType name="MarketTypeVariantEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="D"/><!-- default -->
          <xsd:enumeration value="ASL"/><!-- asian single line -->
          <xsd:enumeration value="ADL"/><!-- asian double line -->
          <xsd:enumeration value="COUP"/><!-- coupon -->
        </xsd:restriction>
      </xsd:simpleType>   

      <xsd:complexType name="GetCouponResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="couponId" nillable="false" type="xsd:int"/>
              <xsd:element name="couponName" nillable="true" type="xsd:string"/>
              <xsd:element name="couponMarketItems" nillable="true" type="types:ArrayOfCouponMarket"/>
              <xsd:element name="parentEventId" nillable="false" type="xsd:int"/>              
              <xsd:element name="errorCode" type="types:GetCouponErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetCouponErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_COUPON_ID"/>
          <xsd:enumeration value="INVALID_LOCALE_DEFAULTING_TO_ENGLISH"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="CouponMarket">
        <xsd:sequence>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="marketName" nillable="true" type="xsd:string"/>
          <xsd:element name="exchangeId" nillable="false" type="xsd:int"/>
          <xsd:element name="parentEventName" nillable="true" type="xsd:string"/>
          <xsd:element name="marketStatus" type="types:MarketStatusEnum"/>
          <xsd:element name="marketType" type="types:MarketTypeEnum"/>
          <xsd:element name="marketTypeVariant" type="types:MarketTypeVariantEnum"/>
          <xsd:element name="marketInfo" nillable="true" type="xsd:string"/>
          <xsd:element name="startTime" type="xsd:dateTime"/>
          <xsd:element name="betDelay" nillable="false" type="xsd:int"/>
          <xsd:element name="couponSelectionItems" nillable="true"
            type="types:ArrayOfCouponSelection"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="CouponSelection">
        <xsd:sequence>
          <xsd:element name="runner" nillable="false" type="types:Runner"/>
          <xsd:element name="backOdds" nillable="true" type="xsd:double"/>
          <xsd:element name="layOdds" nillable="true" type="xsd:double"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfCouponSelection">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0" name="CouponSelection" nillable="true"
            type="types:CouponSelection"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfCouponMarket">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0" name="CouponMarket" nillable="true"
            type="types:CouponMarket"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetCouponReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="couponId" nillable="false" type="xsd:int"/>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="CouponLink">
        <xsd:sequence>
          <xsd:element name="couponId" nillable="false" type="xsd:int"/>
          <xsd:element name="couponName" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfCouponLinks">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="CouponLink" nillable="true" type="types:CouponLink"/>
        </xsd:sequence>
      </xsd:complexType>
      
         <xsd:complexType name="HeartbeatReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="frequency" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="HeartbeatResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:HeartbeatErrorEnum"/>
              <xsd:element name="frequency" nillable="false" type="xsd:int"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="HeartbeatErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="NO_BETS_CANCELLED"/>
          <xsd:enumeration value="BETS_CANCELLED"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      

      <xsd:complexType name="GetMarketResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetMarketErrorEnum"/>
              <xsd:element name="market" nillable="true" type="types:Market"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetMarketErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_MARKET"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
          <xsd:enumeration value="INVALID_LOCALE_DEFAULTING_TO_ENGLISH"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="Market">
        <xsd:sequence>
          <xsd:element name="countryISO3" nillable="true" type="xsd:string"/>
          <xsd:element name="discountAllowed" nillable="false" type="xsd:boolean"/>
          <xsd:element name="eventTypeId" nillable="false" type="xsd:int"/>
          <xsd:element name="lastRefresh" type="xsd:long"/>
          <xsd:element name="marketBaseRate" type="xsd:float"/>
          <xsd:element name="marketDescription" nillable="true" type="xsd:string"/>
          <xsd:element name="marketDescriptionHasDate" nillable="false" type="xsd:boolean"/>          
          <xsd:element name="marketDisplayTime" type="xsd:dateTime"/>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="marketStatus" type="types:MarketStatusEnum"/>
          <xsd:element name="marketSuspendTime" type="xsd:dateTime"/>
          <xsd:element name="marketTime" type="xsd:dateTime"/>
          <xsd:element name="marketType" type="types:MarketTypeEnum"/>
          <xsd:element name="marketTypeVariant" type="types:MarketTypeVariantEnum"/>
          <xsd:element name="menuPath" nillable="true" type="xsd:string"/>
          <xsd:element name="eventHierarchy" nillable="true" type="types:ArrayOfEventId"/>          
          <xsd:element name="name" nillable="true" type="xsd:string"/>
          <xsd:element name="numberOfWinners" nillable="false" type="xsd:int"/>
          <xsd:element name="parentEventId" nillable="false" type="xsd:int"/>
          <xsd:element name="runners" nillable="true" type="types:ArrayOfRunner"/>
          <xsd:element name="unit" nillable="true" type="xsd:string"/>
          <xsd:element name="maxUnitValue" nillable="true" type="xsd:double"/>
          <xsd:element name="minUnitValue" nillable="true" type="xsd:double"/>
          <xsd:element name="interval" nillable="true" type="xsd:double"/>
          <xsd:element name="runnersMayBeAdded" nillable="false" type="xsd:boolean"/>
          <xsd:element name="timezone" nillable="true" type="xsd:string"/>
          <xsd:element name="licenceId" nillable="false" type="xsd:int"/>
          <xsd:element name="couponLinks" nillable="true" type="types:ArrayOfCouponLinks"/>          
          <xsd:element name="bspMarket" nillable="false" type="xsd:boolean"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="MarketStatusEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="ACTIVE"/>
          <xsd:enumeration value="INACTIVE"/>
          <xsd:enumeration value="CLOSED"/>
          <xsd:enumeration value="SUSPENDED"/>
        </xsd:restriction>
      </xsd:simpleType>
      
      <xsd:complexType name="ArrayOfEventId">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="EventId" nillable="true" type="xsd:int"/>
        </xsd:sequence>
      </xsd:complexType>      
      
      <xsd:complexType name="Runner">
        <xsd:sequence>
          <xsd:element name="asianLineId" nillable="false" type="xsd:int"/>
          <xsd:element name="handicap" nillable="false" type="xsd:double"/>
          <xsd:element name="name" nillable="true" type="xsd:string"/>
          <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfRunner">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="Runner" nillable="true" type="types:Runner"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetMarketReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
              <xsd:element name="includeCouponLinks" nillable="false" type="xsd:boolean"/>              
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetMarketPricesResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetMarketPricesErrorEnum"/>
              <xsd:element name="marketPrices" nillable="true" type="types:MarketPrices"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetMarketPricesErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_CURRENCY"/>
          <xsd:enumeration value="INVALID_MARKET"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="MarketPrices">
        <xsd:sequence>
          <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
          <xsd:element name="delay" nillable="false" type="xsd:int"/>
          <xsd:element name="discountAllowed" nillable="false" type="xsd:boolean"/>
          <xsd:element name="lastRefresh" type="xsd:long"/>
          <xsd:element name="marketBaseRate" type="xsd:float"/>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="marketInfo" nillable="true" type="xsd:string"/>
          <xsd:element name="removedRunners" nillable="true" type="xsd:string"/>
          <xsd:element name="marketStatus" type="types:MarketStatusEnum"/>
          <xsd:element name="numberOfWinners" nillable="false" type="xsd:int"/>
          <xsd:element name="bspMarket" nillable="false" type="xsd:boolean"/>          
          <xsd:element name="runnerPrices" nillable="true" type="types:ArrayOfRunnerPrices"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="RunnerPrices">
        <xsd:sequence>
          <xsd:element name="asianLineId" nillable="true" type="xsd:int"/>
          <xsd:element name="bestPricesToBack" nillable="true" type="types:ArrayOfPrice"/>
          <xsd:element name="bestPricesToLay" nillable="true" type="types:ArrayOfPrice"/>
          <xsd:element name="handicap" nillable="true" type="xsd:double"/>
          <xsd:element name="lastPriceMatched" nillable="false" type="xsd:double"/>
          <xsd:element name="reductionFactor" nillable="false" type="xsd:double"/>
          <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
          <xsd:element name="sortOrder" nillable="false" type="xsd:int"/>
          <xsd:element name="totalAmountMatched" nillable="false" type="xsd:double"/>
          <xsd:element name="vacant" nillable="true" type="xsd:boolean"/>
          <xsd:element name="farBSP" nillable="true" type="xsd:double"/>
          <xsd:element name="nearBSP" nillable="true" type="xsd:double"/>
          <xsd:element name="actualBSP" nillable="true" type="xsd:double"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="Price">
        <xsd:sequence>
          <xsd:element name="amountAvailable" nillable="false" type="xsd:double"/>
          <xsd:element name="betType" type="types:BetTypeEnum"/>
          <xsd:element name="depth" nillable="false" type="xsd:int"/>
          <xsd:element name="price" nillable="false" type="xsd:double"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfPrice">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="Price" nillable="true" type="types:Price"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfRunnerPrices">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="RunnerPrices" nillable="true" type="types:RunnerPrices"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetMarketPricesReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      
      <xsd:complexType name="GetAllMarketsResp">
           <xsd:complexContent>
             <xsd:extension base="types:APIResponse">
               <xsd:sequence>
                 <xsd:element name="errorCode" type="types:GetAllMarketsErrorEnum"/>
                 <xsd:element name="marketData" nillable="true" type="xsd:string"/>
                 <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
               </xsd:sequence>
             </xsd:extension>
           </xsd:complexContent>
         </xsd:complexType>
         <xsd:complexType name="GetAllMarketsReq">
           <xsd:complexContent>
             <xsd:extension base="types:APIRequest">
               <xsd:sequence>
                 <xsd:element name="locale" nillable="true" type="xsd:string"/>
                 <xsd:element name="eventTypeIds" nillable="true" type="types:ArrayOfInt"/>
                 <xsd:element name="countries" nillable="true" type="types:ArrayOfCountryCode"/>
                 <xsd:element name="fromDate" nillable="true" type="xsd:dateTime"/>
                 <xsd:element name="toDate" nillable="true" type="xsd:dateTime"/>
               </xsd:sequence>
             </xsd:extension>
           </xsd:complexContent>
         </xsd:complexType>
         <xsd:complexType name="ArrayOfCountryCode">
           <xsd:sequence>
             <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
               name="Country" nillable="true"  type="xsd:string"/>
           </xsd:sequence>
         </xsd:complexType>
         <xsd:simpleType name="GetAllMarketsErrorEnum">
           <xsd:restriction base="xsd:string">
             <xsd:enumeration value="OK"/>
             <xsd:enumeration value="INVALID_COUNTRY_CODE"/>
             <xsd:enumeration value="INVALID_LOCALE"/>
             <xsd:enumeration value="INVALID_EVENT_TYPE_ID"/>
             <xsd:enumeration value="API_ERROR"/>
           </xsd:restriction>
         </xsd:simpleType>
   
         <xsd:complexType name="GetInPlayMarketsResp">
           <xsd:complexContent>
             <xsd:extension base="types:APIResponse">
               <xsd:sequence>
                 <xsd:element name="errorCode" type="types:GetInPlayMarketsErrorEnum"/>
                 <xsd:element name="marketData" nillable="true" type="xsd:string"/>
                 <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
               </xsd:sequence>
             </xsd:extension>
           </xsd:complexContent>
         </xsd:complexType>
         <xsd:complexType name="GetInPlayMarketsReq">
           <xsd:complexContent>
             <xsd:extension base="types:APIRequest">
               <xsd:sequence>
                 <xsd:element name="locale" nillable="true" type="xsd:string"/>
               </xsd:sequence>
             </xsd:extension>
           </xsd:complexContent>
         </xsd:complexType>
         <xsd:simpleType name="GetInPlayMarketsErrorEnum">
           <xsd:restriction base="xsd:string">
             <xsd:enumeration value="OK"/>
             <xsd:enumeration value="INVALID_LOCALE"/>
             <xsd:enumeration value="API_ERROR"/>
           </xsd:restriction>
         </xsd:simpleType>
   
         <xsd:complexType name="GetPrivateMarketsResp">
           <xsd:complexContent>
             <xsd:extension base="types:APIResponse">
               <xsd:sequence>
                 <xsd:element name="errorCode" type="types:GetPrivateMarketsErrorEnum"/>
                 <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
                 <xsd:element name="privateMarkets" nillable="true" type="types:ArrayOfPrivateMarket"/>
                 <xsd:element name="lastRefresh" type="xsd:long"/>
               </xsd:sequence>
             </xsd:extension>
           </xsd:complexContent>
         </xsd:complexType>
         <xsd:complexType name="GetPrivateMarketsReq">
           <xsd:complexContent>
             <xsd:extension base="types:APIRequest">
               <xsd:sequence>
                 <xsd:element name="locale" nillable="true" type="xsd:string"/>
                 <xsd:element name="eventTypeId" nillable="false" type="xsd:int"/>
                 <xsd:element name="marketType" type="types:MarketTypeEnum"/>
               </xsd:sequence>
             </xsd:extension>
           </xsd:complexContent>
         </xsd:complexType>
         <xsd:simpleType name="GetPrivateMarketsErrorEnum">
           <xsd:restriction base="xsd:string">
             <xsd:enumeration value="OK"/>
             <xsd:enumeration value="INVALID_LOCALE"/>
             <xsd:enumeration value="INVALID_EVENT_TYPE_ID"/>
             <xsd:enumeration value="INVALID_MARKET_TYPE"/>
             <xsd:enumeration value="NO_RESULTS"/>
             <xsd:enumeration value="API_ERROR"/>
           </xsd:restriction>
         </xsd:simpleType>
         <xsd:complexType name="PrivateMarket">
           <xsd:sequence>
             <xsd:element name="name" nillable="true" type="xsd:string"/>
             <xsd:element name="marketId" nillable="false" type="xsd:int"/>
             <xsd:element name="menuPath" nillable="true" type="xsd:string"/>
             <xsd:element name="eventHierarchy" nillable="true" type="types:ArrayOfEventId"/>
           </xsd:sequence>
         </xsd:complexType>
         <xsd:complexType name="ArrayOfPrivateMarket">
           <xsd:sequence>
             <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
               name="PrivateMarket" nillable="true" type="types:PrivateMarket"/>
           </xsd:sequence>
         </xsd:complexType>

      <xsd:complexType name="GetCompleteMarketPricesCompressedResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetCompleteMarketPricesErrorEnum"/>
              <xsd:element name="completeMarketPrices" nillable="true" type="xsd:string"/>
              <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetCompleteMarketPricesCompressedReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetCompleteMarketPricesErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_CURRENCY"/>
          <xsd:enumeration value="INVALID_MARKET"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
          <xsd:enumeration value="EVENT_CLOSED"/>
          <xsd:enumeration value="EVENT_SUSPENDED"/>
          <xsd:enumeration value="EVENT_INACTIVE"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="GetMarketTradedVolumeCompressedResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetMarketTradedVolumeCompressedErrorEnum"/>
              <xsd:element name="tradedVolume" nillable="true" type="xsd:string"/>
              <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetMarketTradedVolumeCompressedReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetMarketTradedVolumeCompressedErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_CURRENCY"/>
          <xsd:enumeration value="INVALID_MARKET"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
          <xsd:enumeration value="EVENT_CLOSED"/>
          <xsd:enumeration value="EVENT_SUSPENDED"/>
          <xsd:enumeration value="EVENT_INACTIVE"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="GetMarketPricesCompressedResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetMarketPricesErrorEnum"/>
              <xsd:element name="marketPrices" nillable="true" type="xsd:string"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetMarketPricesCompressedReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="GetCurrentBetsResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="bets" nillable="true" type="types:ArrayOfBet"/>
              <xsd:element name="errorCode" type="types:GetCurrentBetsErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="totalRecordCount" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="GetMUBetsResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="bets" nillable="true" type="types:ArrayOfMUBet"/>
              <xsd:element name="errorCode" type="types:GetMUBetsErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="totalRecordCount" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetMUBetsErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_START_RECORD"/>
          <xsd:enumeration value="INVALID_MARKET_ID"/>
          <xsd:enumeration value="INVALID_RECORD_COUNT"/>
          <xsd:enumeration value="INVALID_BET_STATUS"/>
          <xsd:enumeration value="INVALID_ORDER_BY_FOR_STATUS"/>
          <xsd:enumeration value="TOO_MANY_BETS_REQUESTED"/>          
          <xsd:enumeration value="NO_RESULTS"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="MUBet">
        <xsd:sequence>
          <xsd:element name="asianLineId" nillable="false" type="xsd:int"/>
          <xsd:element name="betId" type="xsd:long"/>
          <xsd:element name="transactionId" type="xsd:long"/>
          <xsd:element name="betStatus" type="types:BetStatusEnum"/>
          <xsd:element name="betType" type="types:BetTypeEnum"/>
          <xsd:element name="betCategoryType" type="types:BetCategoryTypeEnum"/>
          <xsd:element name="betPersistenceType" type="types:BetPersistenceTypeEnum"/>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="matchedDate" type="xsd:dateTime"/>
          <xsd:element name="size" nillable="false" type="xsd:double"/>
          <xsd:element name="bspLiability" nillable="true" type="xsd:double"/>          
          <xsd:element name="placedDate" type="xsd:dateTime"/>
          <xsd:element name="price" nillable="false" type="xsd:double"/>
          <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
          <xsd:element name="handicap" nillable="false" type="xsd:double"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfMUBet">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="MUBet" nillable="true" type="types:MUBet"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetMUBetsReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="betStatus" type="types:BetStatusEnum"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
              <xsd:element name="betIds" nillable="true" type="types:ArrayOfBetId"/>              
              <xsd:element name="orderBy" type="types:BetsOrderByEnum"/>
              <xsd:element name="sortOrder" type="types:SortOrderEnum"/>
              <xsd:element name="recordCount" nillable="false" type="xsd:int"/>
              <xsd:element name="startRecord" nillable="false" type="xsd:int"/>
              <xsd:element name="matchedSince" nillable="true" type="xsd:dateTime"/>
              <xsd:element name="excludeLastSecond" nillable="false" type="xsd:boolean"/>              
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="SortOrderEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="DESC"/>
          <xsd:enumeration value="ASC"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ArrayOfBetId">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="1000" minOccurs="0"
            name="betId" type="xsd:long"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="Bet">
        <xsd:sequence>
          <xsd:element name="asianLineId" nillable="false" type="xsd:int"/>
          <xsd:element name="avgPrice" nillable="false" type="xsd:double"/>
          <xsd:element name="betId" type="xsd:long"/>
          <xsd:element name="betStatus" type="types:BetStatusEnum"/>
          <xsd:element name="betType" type="types:BetTypeEnum"/>
          <xsd:element name="betCategoryType" type="types:BetCategoryTypeEnum"/>
          <xsd:element name="betPersistenceType" type="types:BetPersistenceTypeEnum"/>

          <xsd:element name="cancelledDate" type="xsd:dateTime"/>
          <xsd:element name="lapsedDate" type="xsd:dateTime"/>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="marketName" nillable="true" type="xsd:string"/>
          <xsd:element name="fullMarketName" nillable="true" type="xsd:string"/>          
          <xsd:element name="marketType" type="types:MarketTypeEnum"/>
          <xsd:element name="marketTypeVariant" type="types:MarketTypeVariantEnum"/>
          <xsd:element name="matchedDate" type="xsd:dateTime"/>
          <xsd:element name="matchedSize" nillable="false" type="xsd:double"/>
          <xsd:element name="matches" nillable="true" type="types:ArrayOfMatch"/>
          <xsd:element name="placedDate" type="xsd:dateTime"/>
          <xsd:element name="price" nillable="false" type="xsd:double"/>
          <xsd:element name="bspLiability" nillable="true" type="xsd:double"/>
          <xsd:element name="profitAndLoss" nillable="false" type="xsd:double"/>
          <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
          <xsd:element name="selectionName" nillable="true" type="xsd:string"/>
          <xsd:element name="settledDate" type="xsd:dateTime"/>
          <xsd:element name="remainingSize" nillable="false" type="xsd:double"/>
          <xsd:element name="requestedSize" nillable="false" type="xsd:double"/>
          <xsd:element name="voidedDate" type="xsd:dateTime"/>
          <xsd:element name="handicap" nillable="false" type="xsd:double"/>
        </xsd:sequence>
      </xsd:complexType>
        <xsd:simpleType name="BetStatusEnum">
          <xsd:restriction base="xsd:string">
            <xsd:enumeration value="U"/>
            <xsd:enumeration value="M"/>
            <xsd:enumeration value="S"/>
            <xsd:enumeration value="C"/>
            <xsd:enumeration value="V"/>
            <xsd:enumeration value="L"/>
            <xsd:enumeration value="MU"/>
          </xsd:restriction>
        </xsd:simpleType>
        <xsd:simpleType name="BetCategoryTypeEnum">
          <xsd:restriction base="xsd:string">
            <xsd:enumeration value="E"/>
            <xsd:enumeration value="M"/>
            <xsd:enumeration value="L"/>
            <xsd:enumeration value="NONE"/>            
          </xsd:restriction>
        </xsd:simpleType>
        <xsd:simpleType name="BetPersistenceTypeEnum">
          <xsd:restriction base="xsd:string">
            <xsd:enumeration value="NONE"/>
            <xsd:enumeration value="IP"/>
            <xsd:enumeration value="SP"/>
          </xsd:restriction>
        </xsd:simpleType>
      <xsd:complexType name="Match">
        <xsd:sequence>
          <xsd:element name="betStatus" type="types:BetStatusEnum"/>
          <xsd:element name="matchedDate" type="xsd:dateTime"/>
          <xsd:element name="priceMatched" nillable="false" type="xsd:double"/>
          <xsd:element name="profitLoss" nillable="false" type="xsd:double"/>
          <xsd:element name="settledDate" type="xsd:dateTime"/>
          <xsd:element name="sizeMatched" nillable="false" type="xsd:double"/>
          <xsd:element name="transactionId" type="xsd:long"/>
          <xsd:element name="voidedDate" type="xsd:dateTime"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfMatch">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="Match" nillable="true" type="types:Match"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfBet">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="Bet" nillable="true" type="types:Bet"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="GetCurrentBetsErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_START_RECORD"/>
          <xsd:enumeration value="INVALID_MARKET_ID"/>
          <xsd:enumeration value="INVALID_RECORD_COUNT"/>
          <xsd:enumeration value="INVALID_BET_STATUS"/>
          <xsd:enumeration value="INVALID_ORDER_BY_FOR_STATUS"/>
          <xsd:enumeration value="INVALID_LOCALE_DEFAULTING_TO_ENGLISH"/>          
          <xsd:enumeration value="NO_RESULTS"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="GetCurrentBetsReq">
         <xsd:annotation>
              <xsd:documentation>
                Obtain all bets placed on a given market.  Pass marketId = 0 to obtain bets for all markets.  If
                deatiled is true then also return details of Matches when betStatus = M
              </xsd:documentation>
          </xsd:annotation>
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="betStatus" type="types:BetStatusEnum"/>
              <xsd:element name="detailed" nillable="false" type="xsd:boolean"/>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
              <xsd:element name="timezone" nillable="true" type="xsd:string"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
              <xsd:element name="orderBy" type="types:BetsOrderByEnum"/>
              <xsd:element name="recordCount" nillable="false" type="xsd:int"/>
              <xsd:element name="startRecord" nillable="false" type="xsd:int"/>
              <xsd:element name="noTotalRecordCount" nillable="false" type="xsd:boolean"/>              
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:simpleType name="BetsOrderByEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="NONE"/>
          <xsd:enumeration value="BET_ID"/>
          <xsd:enumeration value="MARKET_NAME"/>
          <xsd:enumeration value="PLACED_DATE"/>
          <xsd:enumeration value="MATCHED_DATE"/>
          <xsd:enumeration value="CANCELLED_DATE"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="GetDetailedAvailableMktDepthResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetDetailedAvailMktDepthErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="priceItems" nillable="true" type="types:ArrayOfAvailabilityInfo"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetDetailedAvailMktDepthErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="NO_RESULTS"/>
          <xsd:enumeration value="SUSPENDED_MARKET"/>
          <xsd:enumeration value="INVALID_MARKET"/>
          <xsd:enumeration value="INVALID_RUNNER"/>
          <xsd:enumeration value="INVALID_ASIAN_LINE"/>
          <xsd:enumeration value="INVALID_CURRENCY"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="AvailabilityInfo">
        <xsd:sequence>
          <xsd:element name="odds" nillable="false" type="xsd:double"/>
          <xsd:element name="totalAvailableBackAmount" nillable="false" type="xsd:double"/>
          <xsd:element name="totalAvailableLayAmount" nillable="false" type="xsd:double"/>
          <xsd:element name="totalBspBackAmount" nillable="false" type="xsd:double"/>
          <xsd:element name="totalBspLayAmount" nillable="false" type="xsd:double"/>          
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfAvailabilityInfo">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="AvailabilityInfo" nillable="true" type="types:AvailabilityInfo"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetDetailedAvailableMktDepthReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="asianLineId" nillable="false" type="xsd:int"/>
              <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
              <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetMarketTradedVolumeResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetMarketTradedVolumeErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="priceItems" nillable="true" type="types:ArrayOfVolumeInfo"/>
			  <xsd:element name="actualBSP" nillable="true" type="xsd:double"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetMarketTradedVolumeErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="NO_RESULTS"/>
          <xsd:enumeration value="INVALID_MARKET"/>
          <xsd:enumeration value="INVALID_RUNNER"/>
          <xsd:enumeration value="INVALID_ASIAN_LINE"/>
          <xsd:enumeration value="MARKET_CLOSED"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
          <xsd:enumeration value="INVALID_CURRENCY"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="VolumeInfo">
        <xsd:sequence>
          <xsd:element name="odds" nillable="false" type="xsd:double"/>
            <xsd:element name="totalMatchedAmount"  nillable="false" type="xsd:double"/>
            <xsd:element name="totalBspBackMatchedAmount"  nillable="false" type="xsd:double"/>
            <xsd:element name="totalBspLiabilityMatchedAmount"  nillable="false" type="xsd:double"/>            
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfVolumeInfo">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="VolumeInfo" nillable="true" type="types:VolumeInfo"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetMarketTradedVolumeReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="asianLineId" nillable="false" type="xsd:int"/>
              <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
              <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetBetHistoryResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="betHistoryItems" nillable="true" type="types:ArrayOfBet"/>
              <xsd:element name="errorCode" type="types:GetBetHistoryErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="totalRecordCount" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetBetHistoryErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_EVENT_TYPE_ID"/>
          <xsd:enumeration value="NO_RESULTS"/>
          <xsd:enumeration value="INVALID_RECORD_COUNT"/>
          <xsd:enumeration value="INVALID_BET_STATUS"/>
          <xsd:enumeration value="INVALID_MARKET_TYPE"/>
          <xsd:enumeration value="INVALID_ORDER_BY"/>
          <xsd:enumeration value="INVALID_START_RECORD"/>
          <xsd:enumeration value="INVALID_LOCALE_DEFAULTING_TO_ENGLISH"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="GetBetHistoryReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="betTypesIncluded" type="types:BetStatusEnum"/>
              <xsd:element name="detailed" nillable="false" type="xsd:boolean"/>
              <xsd:element name="eventTypeIds" nillable="true" type="types:ArrayOfInt"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>              
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
              <xsd:element name="timezone" nillable="true" type="xsd:string"/>
              <xsd:element name="marketTypesIncluded" nillable="true" type="types:ArrayOfMarketTypeEnum"/>
              <xsd:element name="placedDateFrom" type="xsd:dateTime"/>
              <xsd:element name="placedDateTo" type="xsd:dateTime"/>
              <xsd:element name="recordCount" nillable="false" type="xsd:int"/>
              <xsd:element name="sortBetsBy" type="types:BetsOrderByEnum"/>
              <xsd:element name="startRecord" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfMarketTypeEnum">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="MarketTypeEnum" nillable="true" type="types:MarketTypeEnum"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfInt">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="int" nillable="true"  type="xsd:int"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="GetAccountStatementResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetAccountStatementErrorEnum"/>
              <xsd:element name="items" nillable="true" type="types:ArrayOfAccountStatementItem"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="totalRecordCount" nillable="false" type="xsd:int"/>              
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetAccountStatementErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_START_RECORD"/>
          <xsd:enumeration value="INVALID_RECORD_COUNT"/>
          <xsd:enumeration value="INVALID_END_DATE"/>
          <xsd:enumeration value="INVALID_START_DATE"/>
          <xsd:enumeration value="NO_RESULTS"/>
          <xsd:enumeration value="API_ERROR"/>
          <xsd:enumeration value="INVALID_LOCALE_DEFAULTING_TO_ENGLISH"/>          
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="AccountStatementItem">
        <xsd:sequence>
          <xsd:element name="accountBalance" nillable="false" type="xsd:double"/>
          <xsd:element name="amount"  nillable="false" type="xsd:double"/>
          <xsd:element name="avgPrice"  nillable="false" type="xsd:double"/>
          <xsd:element name="betId" type="xsd:long"/>
          <xsd:element name="betSize"  nillable="false" type="xsd:double"/>
          <xsd:element name="betType" type="types:BetTypeEnum"/>
          <xsd:element name="betCategoryType" type="types:BetCategoryTypeEnum"/>
          <xsd:element name="commissionRate" nillable="true" type="xsd:string"/>
          <xsd:element name="eventId" nillable="false" type="xsd:int"/>
          <xsd:element name="eventTypeId" nillable="false" type="xsd:int"/>
          <xsd:element name="fullMarketName" nillable="true" type="xsd:string"/>
          <xsd:element name="grossBetAmount" nillable="false" type="xsd:double"/>
          <xsd:element name="marketName" nillable="true" type="xsd:string"/>
          <xsd:element name="marketType" type="types:MarketTypeEnum"/>
          <xsd:element name="placedDate" type="xsd:dateTime"/>
          <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
          <xsd:element name="selectionName" nillable="true" type="xsd:string"/>
          <xsd:element name="settledDate" type="xsd:dateTime"/>
          <xsd:element name="startDate" type="xsd:dateTime"/>
          <xsd:element name="transactionType" type="types:AccountStatementEnum"/>
          <xsd:element name="transactionId" type="xsd:long"/>          
          <xsd:element name="winLose" type="types:AccountStatementEnum"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="AccountStatementEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="RESULT_WON"/>
          <xsd:enumeration value="RESULT_LOST"/>
          <xsd:enumeration value="RESULT_ERR"/>
          <xsd:enumeration value="RESULT_FIX"/>
          <xsd:enumeration value="RESULT_NOT_APPLICABLE"/>
          <xsd:enumeration value="ACCOUNT_CREDIT"/>
          <xsd:enumeration value="ACCOUNT_DEBIT"/>
          <xsd:enumeration value="COMMISSION_REVERSAL"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ArrayOfAccountStatementItem">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="AccountStatementItem" nillable="true" type="types:AccountStatementItem"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetAccountStatementReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="endDate" type="xsd:dateTime"/>
              <xsd:element name="itemsIncluded" type="types:AccountStatementIncludeEnum"/>
              <xsd:element name="ignoreAutoTransfers" nillable="false" type="xsd:boolean"/>
              <xsd:element name="recordCount" nillable="false" type="xsd:int"/>
              <xsd:element name="startDate" type="xsd:dateTime"/>
              <xsd:element name="startRecord" nillable="false" type="xsd:int"/>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>              
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="AccountStatementIncludeEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="ALL"/>
          <xsd:enumeration value="EXCHANGE"/>
          <xsd:enumeration value="POKER_ROOM"/>
          <xsd:enumeration value="DEPOSITS_WITHDRAWALS"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="GetMarketProfitAndLossResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="annotations" nillable="true" type="types:ArrayOfProfitAndLoss"/>
              <xsd:element name="commissionApplied" nillable="false" type="xsd:double"/>
              <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
              <xsd:element name="errorCode" type="types:GetMarketProfitAndLossErrorEnum"/>
              <xsd:element name="includesSettledBets" nillable="false" type="xsd:boolean"/>
              <xsd:element name="includesBspBets" nillable="false" type="xsd:boolean"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
              <xsd:element name="marketName" nillable="true" type="xsd:string"/>
              <xsd:element name="marketStatus" type="types:MarketStatusEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="unit" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="ProfitAndLoss">
        <xsd:sequence>
          <xsd:element name="futureIfWin" nillable="false" type="xsd:double"/>
          <xsd:element name="ifWin" nillable="false" type="xsd:double"/>
          <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
          <xsd:element name="selectionName" nillable="true" type="xsd:string"/>
          <xsd:element name="worstcaseIfWin" nillable="false" type="xsd:double"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfProfitAndLoss">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="ProfitAndLoss" nillable="true" type="types:ProfitAndLoss"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="GetMarketProfitAndLossErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="INVALID_MARKET"/>
          <xsd:enumeration value="UNSUPPORTED_MARKET_TYPE"/>
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="MARKET_CLOSED"/>
          <xsd:enumeration value="INVALID_LOCALE_DEFAULTING_TO_ENGLISH"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="GetMarketProfitAndLossReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
              <xsd:element name="includeSettledBets" nillable="false" type="xsd:boolean"/>
              <xsd:element name="includeBspBets" nillable="false" type="xsd:boolean"/>
              <xsd:element name="marketID" nillable="false" type="xsd:int"/>
              <xsd:element name="netOfCommission" nillable="false" type="xsd:boolean"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetBetResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="bet" nillable="true" type="types:Bet"/>
              <xsd:element name="errorCode" type="types:GetBetErrorEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetBetErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
          <xsd:enumeration value="BET_ID_INVALID"/>
          <xsd:enumeration value="NO_RESULTS"/>
          <xsd:enumeration value="API_ERROR"/>
          <xsd:enumeration value="INVALID_LOCALE_DEFAULTING_TO_ENGLISH"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="GetBetReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="betId" nillable="false" type="xsd:long"/>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>


      <xsd:complexType name="GetBetLiteResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="betLite" nillable="true" type="types:BetLite"/>
              <xsd:element name="errorCode" type="types:GetBetErrorEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="BetLite">
        <xsd:sequence>
          <xsd:element name="betId" type="xsd:long"/>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="matchedSize" nillable="false" type="xsd:double"/>
          <xsd:element name="remainingSize" nillable="false" type="xsd:double"/>
          <xsd:element name="betStatus" type="types:BetStatusEnum"/>
          <xsd:element name="betCategoryType" type="types:BetCategoryTypeEnum"/>
          <xsd:element name="betPersistenceType" type="types:BetPersistenceTypeEnum"/>
          <xsd:element name="bspLiability" nillable="true" type="xsd:double"/>                    
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfBetLite">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="BetLite" nillable="true" type="types:BetLite"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetBetLiteReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="betId" nillable="false" type="xsd:long"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetBetMatchesLiteReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="betId" nillable="false" type="xsd:long"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetBetMatchesLiteResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="matchLites" nillable="true" type="types:ArrayOfMatchLite"/>
              <xsd:element name="errorCode" type="types:GetBetErrorEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="MatchLite">
        <xsd:sequence>
          <xsd:element name="betStatus" type="types:BetStatusEnum"/>
          <xsd:element name="matchedDate" type="xsd:dateTime"/>
          <xsd:element name="priceMatched" nillable="false" type="xsd:double"/>
          <xsd:element name="sizeMatched" nillable="false" type="xsd:double"/>
          <xsd:element name="transactionId" type="xsd:long"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfMatchLite">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="MatchLite" nillable="true" type="types:MatchLite"/>
        </xsd:sequence>
      </xsd:complexType>
      

      <xsd:complexType name="GetCurrentBetsLiteResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="betLites" nillable="true" type="types:ArrayOfBetLite"/>
              <xsd:element name="errorCode" type="types:GetCurrentBetsErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="totalRecordCount" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetCurrentBetsLiteReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="betStatus" type="types:BetStatusEnum"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
              <xsd:element name="orderBy" type="types:BetsOrderByEnum"/>
              <xsd:element name="recordCount" nillable="false" type="xsd:int"/>
              <xsd:element name="startRecord" nillable="false" type="xsd:int"/>
              <xsd:element name="noTotalRecordCount" nillable="false" type="xsd:boolean"/>              
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="MUBetLite">
        <xsd:sequence>
          <xsd:element name="betId" type="xsd:long"/>
          <xsd:element name="transactionId" type="xsd:long"/>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="size" nillable="false" type="xsd:double"/>
          <xsd:element name="betStatus" type="types:BetStatusEnum"/>
          <xsd:element name="betCategoryType" type="types:BetCategoryTypeEnum"/>
          <xsd:element name="betPersistenceType" type="types:BetPersistenceTypeEnum"/>
          <xsd:element name="bspLiability" nillable="true" type="xsd:double"/>                    
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfMUBetLite">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="MUBetLite" nillable="true" type="types:MUBetLite"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetMUBetsLiteResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="betLites" nillable="true" type="types:ArrayOfMUBetLite"/>
              <xsd:element name="errorCode" type="types:GetMUBetsErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="totalRecordCount" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetMUBetsLiteReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="betStatus" type="types:BetStatusEnum"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
              <xsd:element name="betIds" nillable="true" type="types:ArrayOfBetId"/>              
              <xsd:element name="orderBy" type="types:BetsOrderByEnum"/>
              <xsd:element name="sortOrder" type="types:SortOrderEnum"/>
              <xsd:element name="recordCount" nillable="false" type="xsd:int"/>
              <xsd:element name="startRecord" nillable="false" type="xsd:int"/>
              <xsd:element name="matchedSince" nillable="true" type="xsd:dateTime"/>
              <xsd:element name="excludeLastSecond" nillable="false" type="xsd:boolean"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetMarketInfoResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetMarketErrorEnum"/>
              <xsd:element name="marketLite" nillable="true" type="types:MarketLite"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="MarketLite">
        <xsd:sequence>
          <xsd:element name="marketStatus" type="types:MarketStatusEnum"/>
          <xsd:element name="marketSuspendTime" type="xsd:dateTime"/>
          <xsd:element name="marketTime" type="xsd:dateTime"/>
          <xsd:element name="numberOfRunners" nillable="false" type="xsd:int"/>
          <xsd:element name="delay" nillable="false" type="xsd:int"/>
          <xsd:element name="reconciled" nillable="false" type="xsd:boolean"/>
          <xsd:element name="openForBspBetting" nillable="false" type="xsd:boolean"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetMarketInfoReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="HandicapLine">
        <xsd:complexContent>
          <xsd:extension base="types:ProfitAndLoss">
            <xsd:sequence>
              <xsd:element name="from" nillable="false" type="xsd:double"/>
              <xsd:element name="to" nillable="false" type="xsd:double"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="MultiWinnerOddsLine">
        <xsd:complexContent>
          <xsd:extension base="types:ProfitAndLoss">
            <xsd:sequence>
              <xsd:element name="ifLoss" nillable="false" type="xsd:double"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
    </xsd:schema>

    
    <xsd:schema elementFormDefault="qualified" targetNamespace="http://www.betfair.com/publicapi/v5/BFExchangeService/">
      <xsd:import namespace="http://www.betfair.com/publicapi/types/exchange/v5/"/>
      
      <xsd:element name="getAccountFunds">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetAccountFundsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getAccountFundsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetAccountFundsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="cancelBets">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:CancelBetsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="cancelBetsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:CancelBetsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      
      <xsd:element name="cancelBetsByMarket">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:CancelBetsByMarketReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="cancelBetsByMarketResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:CancelBetsByMarketResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>      
      
         <xsd:element name="heartbeat">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:HeartbeatReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="heartbeatResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:HeartbeatResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      
      <xsd:element name="getSilks">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetSilksReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getSilksResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetSilksResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      
      <xsd:element name="getSilksV2">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetSilksV2Req"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getSilksV2Response">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetSilksV2Resp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="updateBets">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:UpdateBetsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="updateBetsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:UpdateBetsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="placeBets">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:PlaceBetsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="placeBetsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:PlaceBetsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getCoupon">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetCouponReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getCouponResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetCouponResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getMarket">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetMarketReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
        <xsd:element name="getMarketInfo">
              <xsd:complexType>
                <xsd:sequence>
                  <xsd:element name="request" type="types:GetMarketInfoReq"/>
                </xsd:sequence>
              </xsd:complexType>
            </xsd:element>
            <xsd:element name="getMarketInfoResponse">
              <xsd:complexType>
                <xsd:sequence>
                  <xsd:element name="Result" nillable="true" type="types:GetMarketInfoResp"/>
                </xsd:sequence>
              </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMarketResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetMarketResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMarketPrices">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetMarketPricesReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMarketPricesResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetMarketPricesResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getCompleteMarketPricesCompressed">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetCompleteMarketPricesCompressedReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getCompleteMarketPricesCompressedResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetCompleteMarketPricesCompressedResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getMarketTradedVolumeCompressed">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetMarketTradedVolumeCompressedReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMarketTradedVolumeCompressedResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetMarketTradedVolumeCompressedResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getMarketPricesCompressed">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetMarketPricesCompressedReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMarketPricesCompressedResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetMarketPricesCompressedResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      

      <xsd:element name="getAllMarkets">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetAllMarketsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getAllMarketsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetAllMarketsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getInPlayMarkets">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetInPlayMarketsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getInPlayMarketsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetInPlayMarketsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getPrivateMarkets">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetPrivateMarketsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getPrivateMarketsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetPrivateMarketsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>      

      <xsd:element name="getCurrentBets">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetCurrentBetsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getCurrentBetsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetCurrentBetsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

     <xsd:element name="getCurrentBetsLite">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetCurrentBetsLiteReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getCurrentBetsLiteResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetCurrentBetsLiteResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getMUBets">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetMUBetsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMUBetsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetMUBetsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

     <xsd:element name="getMUBetsLite">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetMUBetsLiteReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMUBetsLiteResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetMUBetsLiteResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getDetailAvailableMktDepth">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetDetailedAvailableMktDepthReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getDetailAvailableMktDepthResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetDetailedAvailableMktDepthResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMarketTradedVolume">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetMarketTradedVolumeReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMarketTradedVolumeResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetMarketTradedVolumeResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getBetHistory">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetBetHistoryReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getBetHistoryResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetBetHistoryResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getAccountStatement">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="req" type="types:GetAccountStatementReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getAccountStatementResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetAccountStatementResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMarketProfitAndLoss">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetMarketProfitAndLossReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMarketProfitAndLossResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetMarketProfitAndLossResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getBet">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetBetReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getBetResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetBetResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

   <xsd:element name="getBetLite">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetBetLiteReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getBetLiteResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetBetLiteResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getBetMatchesLite">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetBetMatchesLiteReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getBetMatchesLiteResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetBetMatchesLiteResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

    </xsd:schema>
 
  </wsdl:types>

  <wsdl:message name="getSilksIn">
    <wsdl:part element="tns:getSilks" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getSilksOut">
    <wsdl:part element="tns:getSilksResponse" name="parameters"/>
  </wsdl:message>
  
  <wsdl:message name="getSilksV2In">
    <wsdl:part element="tns:getSilksV2" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getSilksV2Out">
    <wsdl:part element="tns:getSilksV2Response" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getAccountFundsIn">
    <wsdl:part element="tns:getAccountFunds" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getAccountFundsOut">
    <wsdl:part element="tns:getAccountFundsResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="cancelBetsIn">
    <wsdl:part element="tns:cancelBets" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="cancelBetsOut">
    <wsdl:part element="tns:cancelBetsResponse" name="parameters"/>
  </wsdl:message>
   <wsdl:message name="cancelBetsByMarketIn">
      <wsdl:part element="tns:cancelBetsByMarket" name="parameters"/>
    </wsdl:message>
    <wsdl:message name="cancelBetsByMarketOut">
      <wsdl:part element="tns:cancelBetsByMarketResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="updateBetsIn">
    <wsdl:part element="tns:updateBets" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="updateBetsOut">
    <wsdl:part element="tns:updateBetsResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="placeBetsIn">
    <wsdl:part element="tns:placeBets" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="placeBetsOut">
    <wsdl:part element="tns:placeBetsResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketIn">
    <wsdl:part element="tns:getMarket" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketOut">
    <wsdl:part element="tns:getMarketResponse" name="parameters"/>
  </wsdl:message>
   <wsdl:message name="getMarketInfoIn">
      <wsdl:part element="tns:getMarketInfo" name="parameters"/>
    </wsdl:message>
    <wsdl:message name="getMarketInfoOut">
      <wsdl:part element="tns:getMarketInfoResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketPricesIn">
    <wsdl:part element="tns:getMarketPrices" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketPricesOut">
    <wsdl:part element="tns:getMarketPricesResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getCompleteMarketPricesCompressedIn">
    <wsdl:part element="tns:getCompleteMarketPricesCompressed" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getCompleteMarketPricesCompressedOut">
    <wsdl:part element="tns:getCompleteMarketPricesCompressedResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getMarketTradedVolumeCompressedIn">
    <wsdl:part element="tns:getMarketTradedVolumeCompressed" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketTradedVolumeCompressedOut">
    <wsdl:part element="tns:getMarketTradedVolumeCompressedResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getMarketPricesCompressedIn">
    <wsdl:part element="tns:getMarketPricesCompressed" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketPricesCompressedOut">
    <wsdl:part element="tns:getMarketPricesCompressedResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getAllMarketsIn">
    <wsdl:part element="tns:getAllMarkets" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getAllMarketsOut">
    <wsdl:part element="tns:getAllMarketsResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getInPlayMarketsIn">
    <wsdl:part element="tns:getInPlayMarkets" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getInPlayMarketsOut">
    <wsdl:part element="tns:getInPlayMarketsResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getPrivateMarketsIn">
    <wsdl:part element="tns:getPrivateMarkets" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getPrivateMarketsOut">
    <wsdl:part element="tns:getPrivateMarketsResponse" name="parameters"/>
  </wsdl:message>  
  
  <wsdl:message name="getCurrentBetsIn">
    <wsdl:part element="tns:getCurrentBets" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getCurrentBetsOut">
    <wsdl:part element="tns:getCurrentBetsResponse" name="parameters"/>
  </wsdl:message>
  
    <wsdl:message name="getCurrentBetsLiteIn">
      <wsdl:part element="tns:getCurrentBetsLite" name="parameters"/>
    </wsdl:message>
    <wsdl:message name="getCurrentBetsLiteOut">
      <wsdl:part element="tns:getCurrentBetsLiteResponse" name="parameters"/>
    </wsdl:message>


  <wsdl:message name="getMUBetsIn">
    <wsdl:part element="tns:getMUBets" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMUBetsOut">
    <wsdl:part element="tns:getMUBetsResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getMUBetsLiteIn">
    <wsdl:part element="tns:getMUBetsLite" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMUBetsLiteOut">
    <wsdl:part element="tns:getMUBetsLiteResponse" name="parameters"/>
  </wsdl:message>
  
  <wsdl:message name="getDetailAvailableMktDepthIn">
    <wsdl:part element="tns:getDetailAvailableMktDepth" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getDetailAvailableMktDepthOut">
    <wsdl:part element="tns:getDetailAvailableMktDepthResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketTradedVolumeIn">
    <wsdl:part element="tns:getMarketTradedVolume" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketTradedVolumeOut">
    <wsdl:part element="tns:getMarketTradedVolumeResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getBetHistoryIn">
    <wsdl:part element="tns:getBetHistory" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getBetHistoryOut">
    <wsdl:part element="tns:getBetHistoryResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getAccountStatementIn">
    <wsdl:part element="tns:getAccountStatement" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getAccountStatementOut">
    <wsdl:part element="tns:getAccountStatementResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketProfitAndLossIn">
    <wsdl:part element="tns:getMarketProfitAndLoss" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketProfitAndLossOut">
    <wsdl:part element="tns:getMarketProfitAndLossResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getBetIn">
    <wsdl:part element="tns:getBet" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getBetOut">
    <wsdl:part element="tns:getBetResponse" name="parameters"/>
  </wsdl:message>
  
    <wsdl:message name="heartbeatIn">
    <wsdl:part element="tns:heartbeat" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="heartbeatOut">
    <wsdl:part element="tns:heartbeatResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getCouponIn">
    <wsdl:part element="tns:getCoupon" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getCouponOut">
    <wsdl:part element="tns:getCouponResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getBetLiteIn">
    <wsdl:part element="tns:getBetLite" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getBetLiteOut">
    <wsdl:part element="tns:getBetLiteResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getBetMatchesLiteIn">
    <wsdl:part element="tns:getBetMatchesLite" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getBetMatchesLiteOut">
    <wsdl:part element="tns:getBetMatchesLiteResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:portType name="BFExchangeService">
  
	<wsdl:operation name="getSilks">
      <wsdl:input message="tns:getSilksIn" name="getSilksIn"/>
      <wsdl:output message="tns:getSilksOut" name="getSilksOut"/>
    </wsdl:operation>

	<wsdl:operation name="getSilksV2">
      <wsdl:input message="tns:getSilksV2In" name="getSilksV2In"/>
      <wsdl:output message="tns:getSilksV2Out" name="getSilksV2Out"/>
    </wsdl:operation>

    <wsdl:operation name="getAccountFunds">
      <wsdl:input message="tns:getAccountFundsIn" name="getAccountFundsIn"/>
      <wsdl:output message="tns:getAccountFundsOut" name="getAccountFundsOut"/>
    </wsdl:operation>


  <wsdl:operation name="heartbeat">
      <wsdl:input message="tns:heartbeatIn" name="heartbeatIn"/>
      <wsdl:output message="tns:heartbeatOut" name="heartbeatOut"/>
    </wsdl:operation>


    <wsdl:operation name="cancelBets">
      <wsdl:input message="tns:cancelBetsIn" name="cancelBetsIn"/>
      <wsdl:output message="tns:cancelBetsOut" name="cancelBetsOut"/>
    </wsdl:operation>
  <wsdl:operation name="cancelBetsByMarket">
      <wsdl:input message="tns:cancelBetsByMarketIn" name="cancelBetsByMarketIn"/>
      <wsdl:output message="tns:cancelBetsByMarketOut" name="cancelBetsByMarketOut"/>
    </wsdl:operation>    
    <wsdl:operation name="updateBets">
      <wsdl:input message="tns:updateBetsIn" name="updateBetsIn"/>
      <wsdl:output message="tns:updateBetsOut" name="updateBetsOut"/>
    </wsdl:operation>
    <wsdl:operation name="placeBets">
      <wsdl:input message="tns:placeBetsIn" name="placeBetsIn"/>
      <wsdl:output message="tns:placeBetsOut" name="placeBetsOut"/>
    </wsdl:operation>
    <wsdl:operation name="getMarket">
      <wsdl:input message="tns:getMarketIn" name="getMarketIn"/>
      <wsdl:output message="tns:getMarketOut" name="getMarketOut"/>
    </wsdl:operation>
       <wsdl:operation name="getMarketInfo">
          <wsdl:input message="tns:getMarketInfoIn" name="getMarketInfoIn"/>
          <wsdl:output message="tns:getMarketInfoOut" name="getMarketInfoOut"/>
        </wsdl:operation>

    <wsdl:operation name="getMarketPrices">
      <wsdl:input message="tns:getMarketPricesIn" name="getMarketPricesIn"/>
      <wsdl:output message="tns:getMarketPricesOut" name="getMarketPricesOut"/>
    </wsdl:operation>
    <wsdl:operation name="getCompleteMarketPricesCompressed">
      <wsdl:input message="tns:getCompleteMarketPricesCompressedIn" name="getCompleteMarketPricesCompressedIn"/>
      <wsdl:output message="tns:getCompleteMarketPricesCompressedOut" name="getCompleteMarketPricesCompressedOut"/>
    </wsdl:operation>

    <wsdl:operation name="getMarketTradedVolumeCompressed">
      <wsdl:input message="tns:getMarketTradedVolumeCompressedIn" name="getMarketTradedVolumeCompressedIn"/>
      <wsdl:output message="tns:getMarketTradedVolumeCompressedOut" name="getMarketTradedVolumeCompressedOut"/>
    </wsdl:operation>

    <wsdl:operation name="getMarketPricesCompressed">
      <wsdl:input message="tns:getMarketPricesCompressedIn" name="getMarketPricesCompressedIn"/>
      <wsdl:output message="tns:getMarketPricesCompressedOut" name="getMarketPricesCompressedOut"/>
    </wsdl:operation>
    
      <wsdl:operation name="getAllMarkets">
          <wsdl:input message="tns:getAllMarketsIn" name="getAllMarketsIn"/>
          <wsdl:output message="tns:getAllMarketsOut" name="getAllMarketsOut"/>
        </wsdl:operation>
    
        <wsdl:operation name="getInPlayMarkets">
          <wsdl:input message="tns:getInPlayMarketsIn" name="getInPlayMarketsIn"/>
          <wsdl:output message="tns:getInPlayMarketsOut" name="getInPlayMarketsOut"/>
        </wsdl:operation>
    
        <wsdl:operation name="getPrivateMarkets">
          <wsdl:input message="tns:getPrivateMarketsIn" name="getPrivateMarketsIn"/>
          <wsdl:output message="tns:getPrivateMarketsOut" name="getPrivateMarketsOut"/>
    </wsdl:operation>
    
    <wsdl:operation name="getCurrentBets">
      <wsdl:input message="tns:getCurrentBetsIn" name="getCurrentBetsIn"/>
      <wsdl:output message="tns:getCurrentBetsOut" name="getCurrentBetsOut"/>
    </wsdl:operation>

  <wsdl:operation name="getCurrentBetsLite">
      <wsdl:input message="tns:getCurrentBetsLiteIn" name="getCurrentBetsLiteIn"/>
      <wsdl:output message="tns:getCurrentBetsLiteOut" name="getCurrentBetsLiteOut"/>
    </wsdl:operation>


    <wsdl:operation name="getMUBets">
      <wsdl:input message="tns:getMUBetsIn" name="getMUBetsIn"/>
      <wsdl:output message="tns:getMUBetsOut" name="getMUBetsOut"/>
    </wsdl:operation>

    <wsdl:operation name="getMUBetsLite">
      <wsdl:input message="tns:getMUBetsLiteIn" name="getMUBetsLiteIn"/>
      <wsdl:output message="tns:getMUBetsLiteOut" name="getMUBetsLiteOut"/>
    </wsdl:operation>


    <wsdl:operation name="getDetailAvailableMktDepth">
      <wsdl:input message="tns:getDetailAvailableMktDepthIn" name="getDetailAvailableMktDepthIn"/>
      <wsdl:output message="tns:getDetailAvailableMktDepthOut" name="getDetailAvailableMktDepthOut"/>
    </wsdl:operation>
    <wsdl:operation name="getMarketTradedVolume">
      <wsdl:input message="tns:getMarketTradedVolumeIn" name="getMarketTradedVolumeIn"/>
      <wsdl:output message="tns:getMarketTradedVolumeOut" name="getMarketTradedVolumeOut"/>
    </wsdl:operation>
    <wsdl:operation name="getBetHistory">
      <wsdl:input message="tns:getBetHistoryIn" name="getBetHistoryIn"/>
      <wsdl:output message="tns:getBetHistoryOut" name="getBetHistoryOut"/>
    </wsdl:operation>
    <wsdl:operation name="getAccountStatement">
      <wsdl:input message="tns:getAccountStatementIn" name="getAccountStatementIn"/>
      <wsdl:output message="tns:getAccountStatementOut" name="getAccountStatementOut"/>
    </wsdl:operation>
    <wsdl:operation name="getMarketProfitAndLoss">
      <wsdl:input message="tns:getMarketProfitAndLossIn" name="getMarketProfitAndLossIn"/>
      <wsdl:output message="tns:getMarketProfitAndLossOut" name="getMarketProfitAndLossOut"/>
    </wsdl:operation>
    <wsdl:operation name="getBet">
      <wsdl:input message="tns:getBetIn" name="getBetIn"/>
      <wsdl:output message="tns:getBetOut" name="getBetOut"/>
    </wsdl:operation>

    <wsdl:operation name="getCoupon">
      <wsdl:input message="tns:getCouponIn" name="getCouponIn"/>
      <wsdl:output message="tns:getCouponOut" name="getCouponOut"/>
    </wsdl:operation>

    <wsdl:operation name="getBetLite">
      <wsdl:input message="tns:getBetLiteIn" name="getBetLiteIn"/>
      <wsdl:output message="tns:getBetLiteOut" name="getBetLiteOut"/>
    </wsdl:operation>
    <wsdl:operation name="getBetMatchesLite">
      <wsdl:input message="tns:getBetMatchesLiteIn" name="getBetMatchesLiteIn"/>
      <wsdl:output message="tns:getBetMatchesLiteOut" name="getBetMatchesLiteOut"/>
    </wsdl:operation>

  </wsdl:portType>
  <wsdl:binding name="BFExchangeService" type="tns:BFExchangeService">
    <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
    
    <wsdl:operation name="getAccountFunds">
      <soap:operation soapAction="getAccountFunds" style="document"/>
      <wsdl:input name="getAccountFundsIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getAccountFundsOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="cancelBets">
      <soap:operation soapAction="cancelBets" style="document"/>
      <wsdl:input name="cancelBetsIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="cancelBetsOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    
       <wsdl:operation name="cancelBetsByMarket">
          <soap:operation soapAction="cancelBetsByMarket" style="document"/>
          <wsdl:input name="cancelBetsByMarketIn">
            <soap:body use="literal"/>
          </wsdl:input>
          <wsdl:output name="cancelBetsByMarketOut">
            <soap:body use="literal"/>
          </wsdl:output>
    </wsdl:operation>
    
    <wsdl:operation name="updateBets">
      <soap:operation soapAction="updateBets" style="document"/>
      <wsdl:input name="updateBetsIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="updateBetsOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="placeBets">
      <soap:operation soapAction="placeBets" style="document"/>
      <wsdl:input name="placeBetsIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="placeBetsOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getMarket">
      <soap:operation soapAction="getMarket" style="document"/>
      <wsdl:input name="getMarketIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getMarketOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    
        <wsdl:operation name="getMarketInfo">
          <soap:operation soapAction="getMarketInfo" style="document"/>
          <wsdl:input name="getMarketInfoIn">
            <soap:body use="literal"/>
          </wsdl:input>
          <wsdl:output name="getMarketInfoOut">
            <soap:body use="literal"/>
          </wsdl:output>
        </wsdl:operation>

    <wsdl:operation name="getMarketPrices">
      <soap:operation soapAction="getMarketPrices" style="document"/>
      <wsdl:input name="getMarketPricesIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getMarketPricesOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getCompleteMarketPricesCompressed">
      <soap:operation soapAction="getCompleteMarketPricesCompressed" style="document"/>
      <wsdl:input name="getCompleteMarketPricesCompressedIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getCompleteMarketPricesCompressedOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="getMarketTradedVolumeCompressed">
      <soap:operation soapAction="getMarketTradedVolumeCompressed" style="document"/>
      <wsdl:input name="getMarketTradedVolumeCompressedIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getMarketTradedVolumeCompressedOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="getMarketPricesCompressed">
      <soap:operation soapAction="getMarketPricesCompressed" style="document"/>
      <wsdl:input name="getMarketPricesCompressedIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getMarketPricesCompressedOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    
    
        <wsdl:operation name="getAllMarkets">
          <soap:operation soapAction="getAllMarkets" style="document"/>
          <wsdl:input name="getAllMarketsIn">
            <soap:body use="literal"/>
          </wsdl:input>
          <wsdl:output name="getAllMarketsOut">
            <soap:body use="literal"/>
          </wsdl:output>
        </wsdl:operation>
    
        <wsdl:operation name="getInPlayMarkets">
          <soap:operation soapAction="getInPlayMarkets" style="document"/>
          <wsdl:input name="getInPlayMarketsIn">
            <soap:body use="literal"/>
          </wsdl:input>
          <wsdl:output name="getInPlayMarketsOut">
            <soap:body use="literal"/>
          </wsdl:output>
        </wsdl:operation>
    
        <wsdl:operation name="getPrivateMarkets">
          <soap:operation soapAction="getPrivateMarkets" style="document"/>
          <wsdl:input name="getPrivateMarketsIn">
            <soap:body use="literal"/>
          </wsdl:input>
          <wsdl:output name="getPrivateMarketsOut">
            <soap:body use="literal"/>
          </wsdl:output>
        </wsdl:operation>

    <wsdl:operation name="getCurrentBets">
      <soap:operation soapAction="getCurrentBets" style="document"/>
      <wsdl:input name="getCurrentBetsIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getCurrentBetsOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="getCoupon">
      <soap:operation soapAction="getCoupon" style="document"/>
      <wsdl:input name="getCouponIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getCouponOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    
       <wsdl:operation name="getCurrentBetsLite">
          <soap:operation soapAction="getCurrentBetsLite" style="document"/>
          <wsdl:input name="getCurrentBetsLiteIn">
           <soap:body use="literal"/>
          </wsdl:input>
         <wsdl:output name="getCurrentBetsLiteOut">
           <soap:body use="literal"/>
          </wsdl:output>
        </wsdl:operation>


    <wsdl:operation name="getMUBets">
      <soap:operation soapAction="getMUBets" style="document"/>
      <wsdl:input name="getMUBetsIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getMUBetsOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    
        <wsdl:operation name="getMUBetsLite">
          <soap:operation soapAction="getMUBetsLite" style="document"/>
          <wsdl:input name="getMUBetsLiteIn">
            <soap:body use="literal"/>
          </wsdl:input>
          <wsdl:output name="getMUBetsLiteOut">
            <soap:body use="literal"/>
          </wsdl:output>
        </wsdl:operation>

 
    <wsdl:operation name="getDetailAvailableMktDepth">
      <soap:operation soapAction="getDetailAvailableMktDepth" style="document"/>
      <wsdl:input name="getDetailAvailableMktDepthIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getDetailAvailableMktDepthOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getMarketTradedVolume">
      <soap:operation soapAction="getMarketTradedVolume" style="document"/>
      <wsdl:input name="getMarketTradedVolumeIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getMarketTradedVolumeOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getBetHistory">
      <soap:operation soapAction="getBetHistory" style="document"/>
      <wsdl:input name="getBetHistoryIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getBetHistoryOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getAccountStatement">
      <soap:operation soapAction="getAccountStatement" style="document"/>
      <wsdl:input name="getAccountStatementIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getAccountStatementOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getMarketProfitAndLoss">
      <soap:operation soapAction="getMarketProfitAndLoss" style="document"/>
      <wsdl:input name="getMarketProfitAndLossIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getMarketProfitAndLossOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getBet">
      <soap:operation soapAction="getBet" style="document"/>
      <wsdl:input name="getBetIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getBetOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getBetLite">
      <soap:operation soapAction="getBetLite" style="document"/>
      <wsdl:input name="getBetLiteIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getBetLiteOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getBetMatchesLite">
      <soap:operation soapAction="getBetMatchesLite" style="document"/>
      <wsdl:input name="getBetMatchesLiteIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getBetMatchesLiteOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
  
  
    <wsdl:operation name="getSilks">
      <soap:operation soapAction="getSilks" style="document"/>
      <wsdl:input name="getSilksIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getSilksOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>  

    <wsdl:operation name="getSilksV2">
      <soap:operation soapAction="getSilksV2" style="document"/>
      <wsdl:input name="getSilksV2In">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getSilksV2Out">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>  
        
    <wsdl:operation name="heartbeat">
      <soap:operation soapAction="heartbeat" style="document"/>
      <wsdl:input name="heartbeatIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="heartbeatOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    
  </wsdl:binding>
  <wsdl:service name="BFExchangeService">
    <wsdl:port binding="tns:BFExchangeService" name="BFExchangeService">
      <soap:address location="https://api.betfair.com/exchange/v5/BFExchangeService"/>
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>
'''

BFExchangeServiceAus = '''
<?xml version="1.0" encoding="UTF-8"?>

<!--

Copyright 2003-2004 The Sporting Exchange Limited. All rights reserved. 
The presentation, distribution or other dissemination of the information contained herein by The Sporting Exchange Limited (Betfair) is not a license, either expressly or impliedly, to any intellectual property owned or controlled by Betfair.
Save as provided by statute and to the fullest extent permitted by law, the following provisions set out the entire liability of Betfair (including any liability for the acts and omissions of its employees, agents and sub-contractors) to the User in respect of the use of its WSDL file whether in contract, tort, statute, equity or otherwise: 
(a)     The User acknowledges and agrees that (except as expressly provided in this Agreement) the WSDL is provided "AS IS" without warranties of any kind (whether express or implied);
(b)    All conditions, warranties, terms and undertakings (whether express or implied, statutory or otherwise relating to the delivery, performance, quality, uninterrupted use, fitness for purpose, occurrence or reliability of the WSDL are hereby excluded to the fullest extent permitted by law; and 
(c)     Betfair shall not be liable to the User for loss of profit (whether direct or indirect), loss of contracts or goodwill, lost advertising, loss of data or any type of special, indirect, consequential or economic loss (including loss or damage suffered by the User as a result of an action brought by a third party) even if such loss was reasonably foreseeable or Betfair had been advised of the possibility of the User incurring such loss.
No exclusion or limitation set out in this Agreement shall apply in the case of fraud or fraudulent concealment, death or personal injury resulting from the negligence of either party or any of its employees, agents or sub-contractors; and/or any breach of the obligations implied by (as appropriate) section 12 of the Sale of Goods Act 1979, section 2 of the Supply of Goods and Services Act 1982 or section 8 of the Supply of Goods (Implied Terms) Act 1973.

-->

<wsdl:definitions name="BFExchangeService"
  targetNamespace="http://www.betfair.com/publicapi/v5/BFExchangeService/"
  xmlns:types="http://www.betfair.com/publicapi/types/exchange/v5/"
  xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
  xmlns:tns="http://www.betfair.com/publicapi/v5/BFExchangeService/"
  xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <wsdl:types>
    <xsd:schema targetNamespace="http://www.betfair.com/publicapi/types/exchange/v5/">
      <xsd:import namespace="http://schemas.xmlsoap.org/soap/encoding/"/>
      <xsd:complexType abstract="true" name="APIResponse">
        <xsd:sequence>
          <xsd:element name="header" nillable="true" type="types:APIResponseHeader"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="APIResponseHeader">
        <xsd:sequence>
          <xsd:element name="errorCode" type="types:APIErrorEnum"/>
          <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
          <xsd:element name="sessionToken" nillable="true" type="xsd:string"/>
          <xsd:element name="timestamp" type="xsd:dateTime"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="APIErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INTERNAL_ERROR"/>
          <xsd:enumeration value="EXCEEDED_THROTTLE"/>
          <xsd:enumeration value="USER_NOT_SUBSCRIBED_TO_PRODUCT"/>
          <xsd:enumeration value="SUBSCRIPTION_INACTIVE_OR_SUSPENDED"/>
          <xsd:enumeration value="VENDOR_SOFTWARE_INACTIVE"/>
          <xsd:enumeration value="VENDOR_SOFTWARE_INVALID"/>
          <xsd:enumeration value="SERVICE_NOT_AVAILABLE_IN_PRODUCT"/>
          <xsd:enumeration value="NO_SESSION"/>
          <xsd:enumeration value="TOO_MANY_REQUESTS"/>
          <xsd:enumeration value="PRODUCT_REQUIRES_FUNDED_ACCOUNT"/>
          <xsd:enumeration value="SERVICE_NOT_AVAILABLE_FOR_LOGIN_STATUS"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType abstract="true" name="APIRequest">
        <xsd:sequence>
          <xsd:element name="header" nillable="true" type="types:APIRequestHeader"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="APIRequestHeader">
        <xsd:sequence>
          <xsd:element name="clientStamp" type="xsd:long"/>
          <xsd:element name="sessionToken" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="GetAccountFundsResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="availBalance" nillable="false" type="xsd:double"/>
              <xsd:element name="balance" nillable="false" type="xsd:double"/>
              <xsd:element name="commissionRetain" nillable="false" type="xsd:double"/>
              <xsd:element name="creditLimit" nillable="false" type="xsd:double"/>
              <xsd:element name="currentBetfairPoints" nillable="false" type="xsd:int"/>
              <xsd:element name="expoLimit" nillable="false" type="xsd:double"/>
              <xsd:element name="exposure" nillable="false" type="xsd:double"/>
              <xsd:element name="holidaysAvailable" nillable="false" type="xsd:int"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="nextDiscount" nillable="false" type="xsd:double"/>
              <xsd:element name="withdrawBalance" nillable="false" type="xsd:double"/>
              <xsd:element name="errorCode" type="types:GetAccountFundsErrorEnum" />
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetAccountFundsErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="EXPOSURE_CALC_IN_PROGRESS"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="GetAccountFundsReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest"/>
        </xsd:complexContent>
      </xsd:complexType>
      
      <xsd:complexType name="GetSilksResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetSilksErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="marketDisplayDetails" nillable="true" type="types:ArrayOfMarketDisplayDetail"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="MarketDisplayDetail">
        <xsd:sequence>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="racingSilks" nillable="true" type="types:ArrayOfRacingSilk"/>
          <xsd:element name="errorCode" type="types:MarketDisplayErrorEnum"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfMarketDisplayDetail">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="MarketDisplayDetail" nillable="true" type="types:MarketDisplayDetail"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="RacingSilk">
        <xsd:sequence>
          <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
          <xsd:element name="silksURL" nillable="true" type="xsd:string"/>
          <xsd:element name="silksText" nillable="true" type="xsd:string"/>
          <xsd:element name="trainerName" nillable="true" type="xsd:string"/>
          <xsd:element name="ageWeight" nillable="true" type="xsd:string"/>
          <xsd:element name="form" nillable="true" type="xsd:string"/>
          <xsd:element name="daysSince" nillable="false" type="xsd:int"/>
          <xsd:element name="jockeyClaim" nillable="false" type="xsd:int"/>
          <xsd:element name="wearing" nillable="true" type="xsd:string"/>
          <xsd:element name="saddleCloth" nillable="false" type="xsd:int"/>
          <xsd:element name="stallDraw" nillable="false" type="xsd:int"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfRacingSilk">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="RacingSilk" nillable="true" type="types:RacingSilk"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="GetSilksErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_LOCALE"/>
          <xsd:enumeration value="INVALID_NUMBER_OF_MARKETS"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:simpleType name="MarketDisplayErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_MARKET"/>
          <xsd:enumeration value="NO_SILKS_AVAILABLE"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="GetSilksReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
              <xsd:element name="markets" nillable="true" type="types:ArrayOfInt"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      
      <xsd:complexType name="GetSilksV2Resp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetSilksErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="marketDisplayDetails" nillable="true" type="types:ArrayOfMarketDisplayDetailV2"/>
            </xsd:sequence>
          </xsd:extension>   
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="MarketDisplayDetailV2">
        <xsd:sequence>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="racingSilks" nillable="true" type="types:ArrayOfRacingSilkV2"/>
          <xsd:element name="errorCode" type="types:MarketDisplayErrorEnum"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfMarketDisplayDetailV2">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="MarketDisplayDetail" nillable="true" type="types:MarketDisplayDetailV2"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="Breeding">
        <xsd:sequence>
          <xsd:element name="name" nillable="true" type="xsd:string"/>
          <xsd:element name="bred" nillable="true" type="xsd:string"/>
          <xsd:element name="yearBorn" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="RacingSilkV2">
        <xsd:complexContent>
            <xsd:extension base="types:RacingSilk">
              <xsd:sequence>
                <!-- Version 2 fields -->
                <xsd:element name="ownerName" nillable="true" type="xsd:string"/>
                <xsd:element name="jockeyName" nillable="true" type="xsd:string"/>
                <xsd:element name="colour" nillable="true" type="xsd:string"/>
                <xsd:element name="sex" nillable="true" type="xsd:string"/>
                <xsd:element name="bred" nillable="true" type="xsd:string"/>
                <xsd:element name="forecastPriceNumerator" nillable="false" type="xsd:int"/>
                <xsd:element name="forecastPriceDenominator" nillable="false" type="xsd:int"/>
                <xsd:element name="officialRating" nillable="false" type="xsd:int"/>
                <xsd:element name="sire" nillable="true" type="types:Breeding"/>
                <xsd:element name="dam" nillable="true" type="types:Breeding"/>
                <xsd:element name="damSire" nillable="true" type="types:Breeding"/>
              </xsd:sequence>
            </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfRacingSilkV2">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="RacingSilk" nillable="true" type="types:RacingSilkV2"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetSilksV2Req">
        <xsd:complexContent>
          <xsd:extension base="types:GetSilksReq">
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      
      <xsd:complexType name="CancelBetsResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="betResults" nillable="true" type="types:ArrayOfCancelBetsResult"/>
              <xsd:element name="errorCode" type="types:CancelBetsErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="CancelBetsResult">
        <xsd:sequence>
          <xsd:element name="betId" type="xsd:long"/>
          <xsd:element name="resultCode" type="types:CancelBetsResultEnum"/>
          <xsd:element name="sizeCancelled" nillable="false" type="xsd:double"/>
          <xsd:element name="sizeMatched" nillable="false" type="xsd:double"/>
          <xsd:element name="success" nillable="false" type="xsd:boolean"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="CancelBetsResultEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="BET_IN_PROGRESS"/>
          <xsd:enumeration value="BBM_DAEMON_NOT_AVAILABLE"/>
          <xsd:enumeration value="INVALID_BET_ID"/>
          <xsd:enumeration value="UNKNOWN_ERROR"/>
          <xsd:enumeration value="TAKEN_OR_LAPSED"/>
          <xsd:enumeration value="REMAINING_CANCELLED"/>
          <xsd:enumeration value="INPLAY_FORBIDDEN"/>
          <xsd:enumeration value="FROM_COUNTRY_FORBIDDEN"/>
          <xsd:enumeration value="INPLAY_FROM_COUNTRY_FORBIDDEN"/>
          <xsd:enumeration value="SITE_UPGRADE"/>
          <xsd:enumeration value="BET_NOT_CANCELLED"/>
          <xsd:enumeration value="BSP_BETS_CANNOT_BE_CANCELLED"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ArrayOfCancelBetsResult">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="CancelBetsResult" nillable="true" type="types:CancelBetsResult"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="CancelBetsErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="BET_IN_PROGRESS"/>
          <xsd:enumeration value="BBM_DAEMON_NOT_AVAILABLE"/>          
          <xsd:enumeration value="INVALID_NUMER_OF_CANCELLATIONS"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
          <xsd:enumeration value="MARKET_STATUS_INVALID"/>
          <xsd:enumeration value="MARKET_IDS_DONT_MATCH"/>
          <xsd:enumeration value="INVALID_MARKET_ID"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="CancelBetsReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="bets" nillable="true" type="types:ArrayOfCancelBets"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="CancelBets">
        <xsd:sequence>
          <xsd:element name="betId" type="xsd:long"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfCancelBets">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="CancelBets" nillable="true" type="types:CancelBets"/>
        </xsd:sequence>
      </xsd:complexType>
      
      
            <xsd:complexType name="CancelBetsByMarketReq">
              <xsd:complexContent>
                <xsd:extension base="types:APIRequest">
                  <xsd:sequence>
                    <xsd:element name="markets" nillable="true" type="types:ArrayOfInt"/>
                  </xsd:sequence>
                </xsd:extension>
              </xsd:complexContent>
            </xsd:complexType>
            <xsd:complexType name="CancelBetsByMarketResp">
              <xsd:complexContent>
                <xsd:extension base="types:APIResponse">
                  <xsd:sequence>
                    <xsd:element name="results" nillable="true" type="types:ArrayOfCancelBetsByMarketResult"/>
                    <xsd:element name="errorCode" type="types:CancelBetsByMarketErrorEnum"/>
                    <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
                  </xsd:sequence>
                </xsd:extension>
              </xsd:complexContent>
            </xsd:complexType>
            <xsd:simpleType name="CancelBetsByMarketErrorEnum">
              <xsd:restriction base="xsd:string">
                <xsd:enumeration value="OK"/>
                <xsd:enumeration value="INVALID_NUMBER_OF_MARKETS"/>
                <xsd:enumeration value="API_ERROR"/>
              </xsd:restriction>
            </xsd:simpleType>
            <xsd:complexType name="ArrayOfCancelBetsByMarketResult">
              <xsd:sequence>
                <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
                  name="CancelBetsByMarketResult" nillable="true" type="types:CancelBetsByMarketResult"/>
              </xsd:sequence>
            </xsd:complexType>
            <xsd:complexType name="CancelBetsByMarketResult">
              <xsd:sequence>
                <xsd:element name="marketId" type="xsd:int"/>
                <xsd:element name="resultCode" type="types:CancelBetsByMarketResultEnum"/>
              </xsd:sequence>
            </xsd:complexType>
            <xsd:simpleType name="CancelBetsByMarketResultEnum">
              <xsd:restriction base="xsd:string">
                <xsd:enumeration value="OK"/>
                <xsd:enumeration value="MARKET_STATUS_INVALID"/>
                <xsd:enumeration value="UNKNOWN_ERROR"/>
                <xsd:enumeration value="INVALID_MARKET"/>
                <xsd:enumeration value="NO_UNMATCHED_BETS"/>
                <xsd:enumeration value="INPLAY_FORBIDDEN"/>
                <xsd:enumeration value="FROM_COUNTRY_FORBIDDEN"/>
                <xsd:enumeration value="INPLAY_FROM_COUNTRY_FORBIDDEN"/>
                <xsd:enumeration value="SITE_UPGRADE"/>
                <xsd:enumeration value="BET_NOT_CANCELLED"/>
              </xsd:restriction>
      </xsd:simpleType>
      
      <xsd:complexType name="UpdateBetsResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="betResults" nillable="true" type="types:ArrayOfUpdateBetsResult"/>
              <xsd:element name="errorCode" type="types:UpdateBetsErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="UpdateBetsResult">
        <xsd:sequence>
          <xsd:element name="betId" nillable="false" type="xsd:long"/>
          <xsd:element name="newBetId" nillable="true" type="xsd:long"/>
          <xsd:element name="sizeCancelled" nillable="true" type="xsd:double"/>
          <xsd:element name="newSize" nillable="true" type="xsd:double"/>
          <xsd:element name="newPrice" nillable="true" type="xsd:double"/> 
          <xsd:element name="resultCode" type="types:UpdateBetsResultEnum"/>
          <xsd:element name="success" nillable="false" type="xsd:boolean"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="UpdateBetsResultEnum">
        <xsd:restriction base="xsd:string">
            <xsd:enumeration value="OK"/>
            <xsd:enumeration value="BET_IN_PROGRESS"/>
            <xsd:enumeration value="BBM_DAEMON_NOT_AVAILABLE"/>           
            <xsd:enumeration value="BET_CANCELLED_REMAINING_UNMATCHED"/>
            <xsd:enumeration value="BET_CANNOT_BE_ACCEPTED"/>
            <xsd:enumeration value="BET_NOT_CANCELLED"/>
            <xsd:enumeration value="BET_TAKEN_OR_LAPSED"/>
            <xsd:enumeration value="CANCELLED_NOT_PLACED"/>
            <xsd:enumeration value="ERROR_LINE_EXPO_BET_CANCELLED_NOT_PLACED"/>
            <xsd:enumeration value="EVENT_CLOSED_CANNOT_MODIFY_BET"/>
            <xsd:enumeration value="EXCEEDED_EXPOSURE_OR_AVAILABLE_TO_BET_BALANCE"/>
            <xsd:enumeration value="EXPOSURE_CALCULATION_ERROR"/>
            <xsd:enumeration value="EXPOSURE_CALCULATION_IN_PROGRESS"/>
            <xsd:enumeration value="FROM_COUNTRY_ON_EVENT_FORBIDDEN"/>
            <xsd:enumeration value="INPLAY_FROM_COUNTRY_FORBIDDEN"/>
            <xsd:enumeration value="INSUFFICIENT_BALANCE"/>
            <xsd:enumeration value="INVALID_BET_ID"/>
            <xsd:enumeration value="INVALID_OLD_PRICE"/>
            <xsd:enumeration value="INVALID_OLD_SIZE"/>
            <xsd:enumeration value="INVALID_PRICE"/>
            <xsd:enumeration value="INVALID_PRICE_AND_SIZE"/>
            <xsd:enumeration value="INVALID_SIZE"/>
            <xsd:enumeration value="LOSS_LIMIT_EXCEEDED"/>
            <xsd:enumeration value="NEW_BET_SUBMITTED_SUCCESSFULLY"/>
            <xsd:enumeration value="NOT_PLACED_EXPOSURE_EXCEEDED"/>
            <xsd:enumeration value="NOT_PLACED_REMAINING_CANCELLED"/>
            <xsd:enumeration value="OK_REMAINING_CANCELLED"/>
            <xsd:enumeration value="PARTIAL_CANCELLATION"/>
            <xsd:enumeration value="REMAINING_SIZE_CANCELLED"/>
            <xsd:enumeration value="RUNNER_REMOVED"/>
            <xsd:enumeration value="SITE_UPGRADE"/>
            <xsd:enumeration value="UNKNOWN_ERROR"/>
            <xsd:enumeration value="VACANT_TRAP"/>
            <xsd:enumeration value="WRONG_MININUM_PERMITTED_BET_SIZE"/>
            <xsd:enumeration value="BSP_BETS_CANNOT_BE_CANCELLED"/>
            <xsd:enumeration value="BSP_BETTING_NOT_ALLOWED"/>
            <xsd:enumeration value="BSP_BETTING_NOT_SUPPORTED"/>
            <xsd:enumeration value="BSP_INVALID_PRICE_LIMIT"/>
            <xsd:enumeration value="BSP_MOC_BETS_EDITING_NOT_PERMITTED"/>
            <xsd:enumeration value="INVALID_BSP_BET_UPDATE"/>
            <xsd:enumeration value="INVALID_INPUTS"/>
            <xsd:enumeration value="PERSISTENCE_MODIFICATION_SUCCESS"/>
            <xsd:enumeration value="INVALID_NEW_PRICE_LIMIT"/>
            <xsd:enumeration value="BSP_INVALID_PERSISTENCE"/>
		</xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ArrayOfUpdateBetsResult">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="UpdateBetsResult" nillable="true" type="types:UpdateBetsResult"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="UpdateBetsErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
		  <xsd:enumeration value="BET_IN_PROGRESS"/>
		  <xsd:enumeration value="BBM_DAEMON_NOT_AVAILABLE"/>          
          <xsd:enumeration value="ACCOUNT_PENDING"/>
          <xsd:enumeration value="ACCOUNT_SUSPENDED"/>
          <xsd:enumeration value="ACCOUNT_CLOSED"/>
          <xsd:enumeration value="INVALID_NUMBER_OF_BETS"/>
          <xsd:enumeration value="INVALID_MARKET_ID"/>
          <xsd:enumeration value="MARKET_STATUS_INVALID"/>
          <xsd:enumeration value="FROM_COUNTRY_FORBIDDEN"/>
          <xsd:enumeration value="API_ERROR"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="UpdateBetsReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="bets" nillable="true" type="types:ArrayOfUpdateBets"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="UpdateBets">
        <xsd:sequence>
          <xsd:element name="betId" type="xsd:long"/>
          <xsd:element name="newPrice" nillable="true" type="xsd:double"/>
          <xsd:element name="newSize" nillable="false" type="xsd:double"/>
          <xsd:element name="oldPrice" nillable="true" type="xsd:double"/>
          <xsd:element name="oldSize" nillable="false" type="xsd:double"/>
	  <xsd:element name="oldBetPersistenceType" type="types:BetPersistenceTypeEnum"/>          
	  <xsd:element name="newBetPersistenceType" type="types:BetPersistenceTypeEnum"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfUpdateBets">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="UpdateBets" nillable="true" type="types:UpdateBets"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="PlaceBetsResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="betResults" nillable="true" type="types:ArrayOfPlaceBetsResult"/>
              <xsd:element name="errorCode" type="types:PlaceBetsErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="PlaceBetsResult">
        <xsd:sequence>
          <xsd:element name="averagePriceMatched" nillable="false" type="xsd:double"/>
          <xsd:element name="betId" type="xsd:long"/>
          <xsd:element name="resultCode" type="types:PlaceBetsResultEnum"/>
          <xsd:element name="sizeMatched" nillable="false" type="xsd:double"/>
          <xsd:element name="success" nillable="false" type="xsd:boolean"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="PlaceBetsErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="BETWEEN_1_AND_60_BETS_REQUIRED"/>
          <xsd:enumeration value="EVENT_INACTIVE"/>
          <xsd:enumeration value="EVENT_CLOSED"/>
          <xsd:enumeration value="EVENT_SUSPENDED"/>
          <xsd:enumeration value="ACCOUNT_CLOSED"/>
          <xsd:enumeration value="ACCOUNT_SUSPENDED"/>
          <xsd:enumeration value="AUTHORISATION_PENDING"/>
          <xsd:enumeration value="INTERNAL_ERROR"/>
          <xsd:enumeration value="SITE_UPGRADE"/>
          <xsd:enumeration value="BACK_LAY_COMBINATION"/>
          <xsd:enumeration value="INVALID_MARKET"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
          <xsd:enumeration value="DIFFERING_MARKETS"/>
          <xsd:enumeration value="FROM_COUNTRY_FORBIDDEN"/>
          <xsd:enumeration value="ACCOUNT_IS_EXCLUDED"/>
          <xsd:enumeration value="BET_IN_PROGRESS"/>
          <xsd:enumeration value="BBM_DAEMON_NOT_AVAILABLE"/>         
          <xsd:enumeration value="BSP_BETTING_NOT_SUPPORTED"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:simpleType name="PlaceBetsResultEnum">
        <xsd:restriction base="xsd:string">
            <xsd:enumeration value="OK"/>
            <xsd:enumeration value="BET_IN_PROGRESS"/>
            <xsd:enumeration value="BBM_DAEMON_NOT_AVAILABLE"/>         
            <xsd:enumeration value="ACCOUNT_CLOSED"/>
            <xsd:enumeration value="ACCOUNT_IS_EXCLUDED"/>
            <xsd:enumeration value="ACCOUNT_SUSPENDED"/>
            <xsd:enumeration value="CANNOT_ACCEPT_BET"/>
            <xsd:enumeration value="EXPOSURE_CALCULATION_IN_PROGRESS"/>
            <xsd:enumeration value="EXPOSURE_OR_AVAILABLE_BALANCE_EXCEEDED"/>
            <xsd:enumeration value="FROM_COUNTRY_ON_EVENT_FORBIDDEN"/>
            <xsd:enumeration value="INPLAY_FROM_COUNTRY_FORBIDDEN"/>
            <xsd:enumeration value="INSUFFICIENT_BALANCE"/>
            <xsd:enumeration value="INVALID_ASIAN_LINE_ID"/>
            <xsd:enumeration value="INVALID_BET_TYPE"/>
            <xsd:enumeration value="INVALID_INCREMENT"/>
            <xsd:enumeration value="INVALID_MARKET"/>
            <xsd:enumeration value="INVALID_PRICE"/>
            <xsd:enumeration value="INVALID_SELECTION"/>
            <xsd:enumeration value="INVALID_SIZE"/>
            <xsd:enumeration value="LINES_OUT_OF_RANGE"/>
            <xsd:enumeration value="LOSS_LIMIT_EXCEEDED"/>
            <xsd:enumeration value="SELECTION_REMOVED"/>
            <xsd:enumeration value="UNKNOWN_ERROR"/>
            <xsd:enumeration value="VACANT_TRAP"/>      
            <xsd:enumeration value="EVENT_CLOSED"/>
            <xsd:enumeration value="AUTHORISATION_PENDING"/>
            <xsd:enumeration value="BSP_BETTING_NOT_ALLOWED"/>
            <xsd:enumeration value="BSP_BETTING_NOT_SUPPORTED"/>
            <xsd:enumeration value="BSP_MULTIPLE_BETS_NOT_ALLOWED"/>
            <xsd:enumeration value="EVENT_RECONCILED"/>
            <xsd:enumeration value="INVALID_PERSISTENCE"/>
            <xsd:enumeration value="ACCOUNT_LOCKED"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ArrayOfPlaceBetsResult">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="PlaceBetsResult" nillable="true" type="types:PlaceBetsResult"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="PlaceBetsReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="bets" nillable="true" type="types:ArrayOfPlaceBets"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="PlaceBets">
        <xsd:sequence>
          <xsd:element name="asianLineId" nillable="false" type="xsd:int"/>
          <xsd:element name="betType" type="types:BetTypeEnum"/>
          <xsd:element name="betCategoryType" type="types:BetCategoryTypeEnum"/>
          <xsd:element name="betPersistenceType" type="types:BetPersistenceTypeEnum"/>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="price" nillable="false" type="xsd:double"/>
          <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
          <xsd:element name="size" nillable="true" type="xsd:double"/>
          <xsd:element name="bspLiability" nillable="true" type="xsd:double"/>          
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="BetTypeEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="B"/>
          <xsd:enumeration value="L"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ArrayOfPlaceBets">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="PlaceBets" nillable="true" type="types:PlaceBets"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:simpleType name="MarketTypeEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="O"/>
          <xsd:enumeration value="L"/>
          <xsd:enumeration value="R"/>
          <xsd:enumeration value="A"/>
          <xsd:enumeration value="NOT_APPLICABLE"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:simpleType name="MarketTypeVariantEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="D"/><!-- default -->
          <xsd:enumeration value="ASL"/><!-- asian single line -->
          <xsd:enumeration value="ADL"/><!-- asian double line -->
          <xsd:enumeration value="COUP"/><!-- coupon -->
        </xsd:restriction>
      </xsd:simpleType>   

      <xsd:complexType name="GetCouponResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="couponId" nillable="false" type="xsd:int"/>
              <xsd:element name="couponName" nillable="true" type="xsd:string"/>
              <xsd:element name="couponMarketItems" nillable="true" type="types:ArrayOfCouponMarket"/>
              <xsd:element name="parentEventId" nillable="false" type="xsd:int"/>              
              <xsd:element name="errorCode" type="types:GetCouponErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetCouponErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_COUPON_ID"/>
          <xsd:enumeration value="INVALID_LOCALE_DEFAULTING_TO_ENGLISH"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="CouponMarket">
        <xsd:sequence>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="marketName" nillable="true" type="xsd:string"/>
          <xsd:element name="exchangeId" nillable="false" type="xsd:int"/>
          <xsd:element name="parentEventName" nillable="true" type="xsd:string"/>
          <xsd:element name="marketStatus" type="types:MarketStatusEnum"/>
          <xsd:element name="marketType" type="types:MarketTypeEnum"/>
          <xsd:element name="marketTypeVariant" type="types:MarketTypeVariantEnum"/>
          <xsd:element name="marketInfo" nillable="true" type="xsd:string"/>
          <xsd:element name="startTime" type="xsd:dateTime"/>
          <xsd:element name="betDelay" nillable="false" type="xsd:int"/>
          <xsd:element name="couponSelectionItems" nillable="true"
            type="types:ArrayOfCouponSelection"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="CouponSelection">
        <xsd:sequence>
          <xsd:element name="runner" nillable="false" type="types:Runner"/>
          <xsd:element name="backOdds" nillable="true" type="xsd:double"/>
          <xsd:element name="layOdds" nillable="true" type="xsd:double"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfCouponSelection">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0" name="CouponSelection" nillable="true"
            type="types:CouponSelection"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfCouponMarket">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0" name="CouponMarket" nillable="true"
            type="types:CouponMarket"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetCouponReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="couponId" nillable="false" type="xsd:int"/>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="CouponLink">
        <xsd:sequence>
          <xsd:element name="couponId" nillable="false" type="xsd:int"/>
          <xsd:element name="couponName" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfCouponLinks">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="CouponLink" nillable="true" type="types:CouponLink"/>
        </xsd:sequence>
      </xsd:complexType>
      
         <xsd:complexType name="HeartbeatReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="frequency" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="HeartbeatResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:HeartbeatErrorEnum"/>
              <xsd:element name="frequency" nillable="false" type="xsd:int"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="HeartbeatErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="NO_BETS_CANCELLED"/>
          <xsd:enumeration value="BETS_CANCELLED"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      

      <xsd:complexType name="GetMarketResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetMarketErrorEnum"/>
              <xsd:element name="market" nillable="true" type="types:Market"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetMarketErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_MARKET"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
          <xsd:enumeration value="INVALID_LOCALE_DEFAULTING_TO_ENGLISH"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="Market">
        <xsd:sequence>
          <xsd:element name="countryISO3" nillable="true" type="xsd:string"/>
          <xsd:element name="discountAllowed" nillable="false" type="xsd:boolean"/>
          <xsd:element name="eventTypeId" nillable="false" type="xsd:int"/>
          <xsd:element name="lastRefresh" type="xsd:long"/>
          <xsd:element name="marketBaseRate" type="xsd:float"/>
          <xsd:element name="marketDescription" nillable="true" type="xsd:string"/>
          <xsd:element name="marketDescriptionHasDate" nillable="false" type="xsd:boolean"/>          
          <xsd:element name="marketDisplayTime" type="xsd:dateTime"/>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="marketStatus" type="types:MarketStatusEnum"/>
          <xsd:element name="marketSuspendTime" type="xsd:dateTime"/>
          <xsd:element name="marketTime" type="xsd:dateTime"/>
          <xsd:element name="marketType" type="types:MarketTypeEnum"/>
          <xsd:element name="marketTypeVariant" type="types:MarketTypeVariantEnum"/>
          <xsd:element name="menuPath" nillable="true" type="xsd:string"/>
          <xsd:element name="eventHierarchy" nillable="true" type="types:ArrayOfEventId"/>          
          <xsd:element name="name" nillable="true" type="xsd:string"/>
          <xsd:element name="numberOfWinners" nillable="false" type="xsd:int"/>
          <xsd:element name="parentEventId" nillable="false" type="xsd:int"/>
          <xsd:element name="runners" nillable="true" type="types:ArrayOfRunner"/>
          <xsd:element name="unit" nillable="true" type="xsd:string"/>
          <xsd:element name="maxUnitValue" nillable="true" type="xsd:double"/>
          <xsd:element name="minUnitValue" nillable="true" type="xsd:double"/>
          <xsd:element name="interval" nillable="true" type="xsd:double"/>
          <xsd:element name="runnersMayBeAdded" nillable="false" type="xsd:boolean"/>
          <xsd:element name="timezone" nillable="true" type="xsd:string"/>
          <xsd:element name="licenceId" nillable="false" type="xsd:int"/>
          <xsd:element name="couponLinks" nillable="true" type="types:ArrayOfCouponLinks"/>          
          <xsd:element name="bspMarket" nillable="false" type="xsd:boolean"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="MarketStatusEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="ACTIVE"/>
          <xsd:enumeration value="INACTIVE"/>
          <xsd:enumeration value="CLOSED"/>
          <xsd:enumeration value="SUSPENDED"/>
        </xsd:restriction>
      </xsd:simpleType>
      
      <xsd:complexType name="ArrayOfEventId">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="EventId" nillable="true" type="xsd:int"/>
        </xsd:sequence>
      </xsd:complexType>      
      
      <xsd:complexType name="Runner">
        <xsd:sequence>
          <xsd:element name="asianLineId" nillable="false" type="xsd:int"/>
          <xsd:element name="handicap" nillable="false" type="xsd:double"/>
          <xsd:element name="name" nillable="true" type="xsd:string"/>
          <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfRunner">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="Runner" nillable="true" type="types:Runner"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetMarketReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
              <xsd:element name="includeCouponLinks" nillable="false" type="xsd:boolean"/>              
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetMarketPricesResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetMarketPricesErrorEnum"/>
              <xsd:element name="marketPrices" nillable="true" type="types:MarketPrices"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetMarketPricesErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_CURRENCY"/>
          <xsd:enumeration value="INVALID_MARKET"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="MarketPrices">
        <xsd:sequence>
          <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
          <xsd:element name="delay" nillable="false" type="xsd:int"/>
          <xsd:element name="discountAllowed" nillable="false" type="xsd:boolean"/>
          <xsd:element name="lastRefresh" type="xsd:long"/>
          <xsd:element name="marketBaseRate" type="xsd:float"/>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="marketInfo" nillable="true" type="xsd:string"/>
          <xsd:element name="removedRunners" nillable="true" type="xsd:string"/>
          <xsd:element name="marketStatus" type="types:MarketStatusEnum"/>
          <xsd:element name="numberOfWinners" nillable="false" type="xsd:int"/>
          <xsd:element name="bspMarket" nillable="false" type="xsd:boolean"/>          
          <xsd:element name="runnerPrices" nillable="true" type="types:ArrayOfRunnerPrices"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="RunnerPrices">
        <xsd:sequence>
          <xsd:element name="asianLineId" nillable="true" type="xsd:int"/>
          <xsd:element name="bestPricesToBack" nillable="true" type="types:ArrayOfPrice"/>
          <xsd:element name="bestPricesToLay" nillable="true" type="types:ArrayOfPrice"/>
          <xsd:element name="handicap" nillable="true" type="xsd:double"/>
          <xsd:element name="lastPriceMatched" nillable="false" type="xsd:double"/>
          <xsd:element name="reductionFactor" nillable="false" type="xsd:double"/>
          <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
          <xsd:element name="sortOrder" nillable="false" type="xsd:int"/>
          <xsd:element name="totalAmountMatched" nillable="false" type="xsd:double"/>
          <xsd:element name="vacant" nillable="true" type="xsd:boolean"/>
          <xsd:element name="farBSP" nillable="true" type="xsd:double"/>
          <xsd:element name="nearBSP" nillable="true" type="xsd:double"/>
          <xsd:element name="actualBSP" nillable="true" type="xsd:double"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="Price">
        <xsd:sequence>
          <xsd:element name="amountAvailable" nillable="false" type="xsd:double"/>
          <xsd:element name="betType" type="types:BetTypeEnum"/>
          <xsd:element name="depth" nillable="false" type="xsd:int"/>
          <xsd:element name="price" nillable="false" type="xsd:double"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfPrice">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="Price" nillable="true" type="types:Price"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfRunnerPrices">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="RunnerPrices" nillable="true" type="types:RunnerPrices"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetMarketPricesReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      
      <xsd:complexType name="GetAllMarketsResp">
           <xsd:complexContent>
             <xsd:extension base="types:APIResponse">
               <xsd:sequence>
                 <xsd:element name="errorCode" type="types:GetAllMarketsErrorEnum"/>
                 <xsd:element name="marketData" nillable="true" type="xsd:string"/>
                 <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
               </xsd:sequence>
             </xsd:extension>
           </xsd:complexContent>
         </xsd:complexType>
         <xsd:complexType name="GetAllMarketsReq">
           <xsd:complexContent>
             <xsd:extension base="types:APIRequest">
               <xsd:sequence>
                 <xsd:element name="locale" nillable="true" type="xsd:string"/>
                 <xsd:element name="eventTypeIds" nillable="true" type="types:ArrayOfInt"/>
                 <xsd:element name="countries" nillable="true" type="types:ArrayOfCountryCode"/>
                 <xsd:element name="fromDate" nillable="true" type="xsd:dateTime"/>
                 <xsd:element name="toDate" nillable="true" type="xsd:dateTime"/>
               </xsd:sequence>
             </xsd:extension>
           </xsd:complexContent>
         </xsd:complexType>
         <xsd:complexType name="ArrayOfCountryCode">
           <xsd:sequence>
             <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
               name="Country" nillable="true"  type="xsd:string"/>
           </xsd:sequence>
         </xsd:complexType>
         <xsd:simpleType name="GetAllMarketsErrorEnum">
           <xsd:restriction base="xsd:string">
             <xsd:enumeration value="OK"/>
             <xsd:enumeration value="INVALID_COUNTRY_CODE"/>
             <xsd:enumeration value="INVALID_LOCALE"/>
             <xsd:enumeration value="INVALID_EVENT_TYPE_ID"/>
             <xsd:enumeration value="API_ERROR"/>
           </xsd:restriction>
         </xsd:simpleType>
   
         <xsd:complexType name="GetInPlayMarketsResp">
           <xsd:complexContent>
             <xsd:extension base="types:APIResponse">
               <xsd:sequence>
                 <xsd:element name="errorCode" type="types:GetInPlayMarketsErrorEnum"/>
                 <xsd:element name="marketData" nillable="true" type="xsd:string"/>
                 <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
               </xsd:sequence>
             </xsd:extension>
           </xsd:complexContent>
         </xsd:complexType>
         <xsd:complexType name="GetInPlayMarketsReq">
           <xsd:complexContent>
             <xsd:extension base="types:APIRequest">
               <xsd:sequence>
                 <xsd:element name="locale" nillable="true" type="xsd:string"/>
               </xsd:sequence>
             </xsd:extension>
           </xsd:complexContent>
         </xsd:complexType>
         <xsd:simpleType name="GetInPlayMarketsErrorEnum">
           <xsd:restriction base="xsd:string">
             <xsd:enumeration value="OK"/>
             <xsd:enumeration value="INVALID_LOCALE"/>
             <xsd:enumeration value="API_ERROR"/>
           </xsd:restriction>
         </xsd:simpleType>
   
         <xsd:complexType name="GetPrivateMarketsResp">
           <xsd:complexContent>
             <xsd:extension base="types:APIResponse">
               <xsd:sequence>
                 <xsd:element name="errorCode" type="types:GetPrivateMarketsErrorEnum"/>
                 <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
                 <xsd:element name="privateMarkets" nillable="true" type="types:ArrayOfPrivateMarket"/>
                 <xsd:element name="lastRefresh" type="xsd:long"/>
               </xsd:sequence>
             </xsd:extension>
           </xsd:complexContent>
         </xsd:complexType>
         <xsd:complexType name="GetPrivateMarketsReq">
           <xsd:complexContent>
             <xsd:extension base="types:APIRequest">
               <xsd:sequence>
                 <xsd:element name="locale" nillable="true" type="xsd:string"/>
                 <xsd:element name="eventTypeId" nillable="false" type="xsd:int"/>
                 <xsd:element name="marketType" type="types:MarketTypeEnum"/>
               </xsd:sequence>
             </xsd:extension>
           </xsd:complexContent>
         </xsd:complexType>
         <xsd:simpleType name="GetPrivateMarketsErrorEnum">
           <xsd:restriction base="xsd:string">
             <xsd:enumeration value="OK"/>
             <xsd:enumeration value="INVALID_LOCALE"/>
             <xsd:enumeration value="INVALID_EVENT_TYPE_ID"/>
             <xsd:enumeration value="INVALID_MARKET_TYPE"/>
             <xsd:enumeration value="NO_RESULTS"/>
             <xsd:enumeration value="API_ERROR"/>
           </xsd:restriction>
         </xsd:simpleType>
         <xsd:complexType name="PrivateMarket">
           <xsd:sequence>
             <xsd:element name="name" nillable="true" type="xsd:string"/>
             <xsd:element name="marketId" nillable="false" type="xsd:int"/>
             <xsd:element name="menuPath" nillable="true" type="xsd:string"/>
             <xsd:element name="eventHierarchy" nillable="true" type="types:ArrayOfEventId"/>
           </xsd:sequence>
         </xsd:complexType>
         <xsd:complexType name="ArrayOfPrivateMarket">
           <xsd:sequence>
             <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
               name="PrivateMarket" nillable="true" type="types:PrivateMarket"/>
           </xsd:sequence>
         </xsd:complexType>

      <xsd:complexType name="GetCompleteMarketPricesCompressedResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetCompleteMarketPricesErrorEnum"/>
              <xsd:element name="completeMarketPrices" nillable="true" type="xsd:string"/>
              <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetCompleteMarketPricesCompressedReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetCompleteMarketPricesErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_CURRENCY"/>
          <xsd:enumeration value="INVALID_MARKET"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
          <xsd:enumeration value="EVENT_CLOSED"/>
          <xsd:enumeration value="EVENT_SUSPENDED"/>
          <xsd:enumeration value="EVENT_INACTIVE"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="GetMarketTradedVolumeCompressedResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetMarketTradedVolumeCompressedErrorEnum"/>
              <xsd:element name="tradedVolume" nillable="true" type="xsd:string"/>
              <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetMarketTradedVolumeCompressedReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetMarketTradedVolumeCompressedErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_CURRENCY"/>
          <xsd:enumeration value="INVALID_MARKET"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
          <xsd:enumeration value="EVENT_CLOSED"/>
          <xsd:enumeration value="EVENT_SUSPENDED"/>
          <xsd:enumeration value="EVENT_INACTIVE"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="GetMarketPricesCompressedResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetMarketPricesErrorEnum"/>
              <xsd:element name="marketPrices" nillable="true" type="xsd:string"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetMarketPricesCompressedReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="GetCurrentBetsResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="bets" nillable="true" type="types:ArrayOfBet"/>
              <xsd:element name="errorCode" type="types:GetCurrentBetsErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="totalRecordCount" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="GetMUBetsResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="bets" nillable="true" type="types:ArrayOfMUBet"/>
              <xsd:element name="errorCode" type="types:GetMUBetsErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="totalRecordCount" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetMUBetsErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_START_RECORD"/>
          <xsd:enumeration value="INVALID_MARKET_ID"/>
          <xsd:enumeration value="INVALID_RECORD_COUNT"/>
          <xsd:enumeration value="INVALID_BET_STATUS"/>
          <xsd:enumeration value="INVALID_ORDER_BY_FOR_STATUS"/>
          <xsd:enumeration value="TOO_MANY_BETS_REQUESTED"/>          
          <xsd:enumeration value="NO_RESULTS"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="MUBet">
        <xsd:sequence>
          <xsd:element name="asianLineId" nillable="false" type="xsd:int"/>
          <xsd:element name="betId" type="xsd:long"/>
          <xsd:element name="transactionId" type="xsd:long"/>
          <xsd:element name="betStatus" type="types:BetStatusEnum"/>
          <xsd:element name="betType" type="types:BetTypeEnum"/>
          <xsd:element name="betCategoryType" type="types:BetCategoryTypeEnum"/>
          <xsd:element name="betPersistenceType" type="types:BetPersistenceTypeEnum"/>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="matchedDate" type="xsd:dateTime"/>
          <xsd:element name="size" nillable="false" type="xsd:double"/>
          <xsd:element name="bspLiability" nillable="true" type="xsd:double"/>          
          <xsd:element name="placedDate" type="xsd:dateTime"/>
          <xsd:element name="price" nillable="false" type="xsd:double"/>
          <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
          <xsd:element name="handicap" nillable="false" type="xsd:double"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfMUBet">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="MUBet" nillable="true" type="types:MUBet"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetMUBetsReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="betStatus" type="types:BetStatusEnum"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
              <xsd:element name="betIds" nillable="true" type="types:ArrayOfBetId"/>              
              <xsd:element name="orderBy" type="types:BetsOrderByEnum"/>
              <xsd:element name="sortOrder" type="types:SortOrderEnum"/>
              <xsd:element name="recordCount" nillable="false" type="xsd:int"/>
              <xsd:element name="startRecord" nillable="false" type="xsd:int"/>
              <xsd:element name="matchedSince" nillable="true" type="xsd:dateTime"/>
              <xsd:element name="excludeLastSecond" nillable="false" type="xsd:boolean"/>              
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="SortOrderEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="DESC"/>
          <xsd:enumeration value="ASC"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ArrayOfBetId">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="1000" minOccurs="0"
            name="betId" type="xsd:long"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="Bet">
        <xsd:sequence>
          <xsd:element name="asianLineId" nillable="false" type="xsd:int"/>
          <xsd:element name="avgPrice" nillable="false" type="xsd:double"/>
          <xsd:element name="betId" type="xsd:long"/>
          <xsd:element name="betStatus" type="types:BetStatusEnum"/>
          <xsd:element name="betType" type="types:BetTypeEnum"/>
          <xsd:element name="betCategoryType" type="types:BetCategoryTypeEnum"/>
          <xsd:element name="betPersistenceType" type="types:BetPersistenceTypeEnum"/>

          <xsd:element name="cancelledDate" type="xsd:dateTime"/>
          <xsd:element name="lapsedDate" type="xsd:dateTime"/>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="marketName" nillable="true" type="xsd:string"/>
          <xsd:element name="fullMarketName" nillable="true" type="xsd:string"/>          
          <xsd:element name="marketType" type="types:MarketTypeEnum"/>
          <xsd:element name="marketTypeVariant" type="types:MarketTypeVariantEnum"/>
          <xsd:element name="matchedDate" type="xsd:dateTime"/>
          <xsd:element name="matchedSize" nillable="false" type="xsd:double"/>
          <xsd:element name="matches" nillable="true" type="types:ArrayOfMatch"/>
          <xsd:element name="placedDate" type="xsd:dateTime"/>
          <xsd:element name="price" nillable="false" type="xsd:double"/>
          <xsd:element name="bspLiability" nillable="true" type="xsd:double"/>
          <xsd:element name="profitAndLoss" nillable="false" type="xsd:double"/>
          <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
          <xsd:element name="selectionName" nillable="true" type="xsd:string"/>
          <xsd:element name="settledDate" type="xsd:dateTime"/>
          <xsd:element name="remainingSize" nillable="false" type="xsd:double"/>
          <xsd:element name="requestedSize" nillable="false" type="xsd:double"/>
          <xsd:element name="voidedDate" type="xsd:dateTime"/>
          <xsd:element name="handicap" nillable="false" type="xsd:double"/>
        </xsd:sequence>
      </xsd:complexType>
        <xsd:simpleType name="BetStatusEnum">
          <xsd:restriction base="xsd:string">
            <xsd:enumeration value="U"/>
            <xsd:enumeration value="M"/>
            <xsd:enumeration value="S"/>
            <xsd:enumeration value="C"/>
            <xsd:enumeration value="V"/>
            <xsd:enumeration value="L"/>
            <xsd:enumeration value="MU"/>
          </xsd:restriction>
        </xsd:simpleType>
        <xsd:simpleType name="BetCategoryTypeEnum">
          <xsd:restriction base="xsd:string">
            <xsd:enumeration value="E"/>
            <xsd:enumeration value="M"/>
            <xsd:enumeration value="L"/>
            <xsd:enumeration value="NONE"/>            
          </xsd:restriction>
        </xsd:simpleType>
        <xsd:simpleType name="BetPersistenceTypeEnum">
          <xsd:restriction base="xsd:string">
            <xsd:enumeration value="NONE"/>
            <xsd:enumeration value="IP"/>
            <xsd:enumeration value="SP"/>
          </xsd:restriction>
        </xsd:simpleType>
      <xsd:complexType name="Match">
        <xsd:sequence>
          <xsd:element name="betStatus" type="types:BetStatusEnum"/>
          <xsd:element name="matchedDate" type="xsd:dateTime"/>
          <xsd:element name="priceMatched" nillable="false" type="xsd:double"/>
          <xsd:element name="profitLoss" nillable="false" type="xsd:double"/>
          <xsd:element name="settledDate" type="xsd:dateTime"/>
          <xsd:element name="sizeMatched" nillable="false" type="xsd:double"/>
          <xsd:element name="transactionId" type="xsd:long"/>
          <xsd:element name="voidedDate" type="xsd:dateTime"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfMatch">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="Match" nillable="true" type="types:Match"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfBet">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="Bet" nillable="true" type="types:Bet"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="GetCurrentBetsErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_START_RECORD"/>
          <xsd:enumeration value="INVALID_MARKET_ID"/>
          <xsd:enumeration value="INVALID_RECORD_COUNT"/>
          <xsd:enumeration value="INVALID_BET_STATUS"/>
          <xsd:enumeration value="INVALID_ORDER_BY_FOR_STATUS"/>
          <xsd:enumeration value="INVALID_LOCALE_DEFAULTING_TO_ENGLISH"/>          
          <xsd:enumeration value="NO_RESULTS"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="GetCurrentBetsReq">
         <xsd:annotation>
              <xsd:documentation>
                Obtain all bets placed on a given market.  Pass marketId = 0 to obtain bets for all markets.  If
                deatiled is true then also return details of Matches when betStatus = M
              </xsd:documentation>
          </xsd:annotation>
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="betStatus" type="types:BetStatusEnum"/>
              <xsd:element name="detailed" nillable="false" type="xsd:boolean"/>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
              <xsd:element name="timezone" nillable="true" type="xsd:string"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
              <xsd:element name="orderBy" type="types:BetsOrderByEnum"/>
              <xsd:element name="recordCount" nillable="false" type="xsd:int"/>
              <xsd:element name="startRecord" nillable="false" type="xsd:int"/>
              <xsd:element name="noTotalRecordCount" nillable="false" type="xsd:boolean"/>              
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:simpleType name="BetsOrderByEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="NONE"/>
          <xsd:enumeration value="BET_ID"/>
          <xsd:enumeration value="MARKET_NAME"/>
          <xsd:enumeration value="PLACED_DATE"/>
          <xsd:enumeration value="MATCHED_DATE"/>
          <xsd:enumeration value="CANCELLED_DATE"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="GetDetailedAvailableMktDepthResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetDetailedAvailMktDepthErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="priceItems" nillable="true" type="types:ArrayOfAvailabilityInfo"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetDetailedAvailMktDepthErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="NO_RESULTS"/>
          <xsd:enumeration value="SUSPENDED_MARKET"/>
          <xsd:enumeration value="INVALID_MARKET"/>
          <xsd:enumeration value="INVALID_RUNNER"/>
          <xsd:enumeration value="INVALID_ASIAN_LINE"/>
          <xsd:enumeration value="INVALID_CURRENCY"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="AvailabilityInfo">
        <xsd:sequence>
          <xsd:element name="odds" nillable="false" type="xsd:double"/>
          <xsd:element name="totalAvailableBackAmount" nillable="false" type="xsd:double"/>
          <xsd:element name="totalAvailableLayAmount" nillable="false" type="xsd:double"/>
          <xsd:element name="totalBspBackAmount" nillable="false" type="xsd:double"/>
          <xsd:element name="totalBspLayAmount" nillable="false" type="xsd:double"/>          
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfAvailabilityInfo">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="AvailabilityInfo" nillable="true" type="types:AvailabilityInfo"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetDetailedAvailableMktDepthReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="asianLineId" nillable="false" type="xsd:int"/>
              <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
              <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetMarketTradedVolumeResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetMarketTradedVolumeErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="priceItems" nillable="true" type="types:ArrayOfVolumeInfo"/>
			  <xsd:element name="actualBSP" nillable="true" type="xsd:double"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetMarketTradedVolumeErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="NO_RESULTS"/>
          <xsd:enumeration value="INVALID_MARKET"/>
          <xsd:enumeration value="INVALID_RUNNER"/>
          <xsd:enumeration value="INVALID_ASIAN_LINE"/>
          <xsd:enumeration value="MARKET_CLOSED"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
          <xsd:enumeration value="INVALID_CURRENCY"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="VolumeInfo">
        <xsd:sequence>
          <xsd:element name="odds" nillable="false" type="xsd:double"/>
            <xsd:element name="totalMatchedAmount"  nillable="false" type="xsd:double"/>
            <xsd:element name="totalBspBackMatchedAmount"  nillable="false" type="xsd:double"/>
            <xsd:element name="totalBspLiabilityMatchedAmount"  nillable="false" type="xsd:double"/>            
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfVolumeInfo">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="VolumeInfo" nillable="true" type="types:VolumeInfo"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetMarketTradedVolumeReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="asianLineId" nillable="false" type="xsd:int"/>
              <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
              <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetBetHistoryResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="betHistoryItems" nillable="true" type="types:ArrayOfBet"/>
              <xsd:element name="errorCode" type="types:GetBetHistoryErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="totalRecordCount" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetBetHistoryErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_EVENT_TYPE_ID"/>
          <xsd:enumeration value="NO_RESULTS"/>
          <xsd:enumeration value="INVALID_RECORD_COUNT"/>
          <xsd:enumeration value="INVALID_BET_STATUS"/>
          <xsd:enumeration value="INVALID_MARKET_TYPE"/>
          <xsd:enumeration value="INVALID_ORDER_BY"/>
          <xsd:enumeration value="INVALID_START_RECORD"/>
          <xsd:enumeration value="INVALID_LOCALE_DEFAULTING_TO_ENGLISH"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="GetBetHistoryReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="betTypesIncluded" type="types:BetStatusEnum"/>
              <xsd:element name="detailed" nillable="false" type="xsd:boolean"/>
              <xsd:element name="eventTypeIds" nillable="true" type="types:ArrayOfInt"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>              
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
              <xsd:element name="timezone" nillable="true" type="xsd:string"/>
              <xsd:element name="marketTypesIncluded" nillable="true" type="types:ArrayOfMarketTypeEnum"/>
              <xsd:element name="placedDateFrom" type="xsd:dateTime"/>
              <xsd:element name="placedDateTo" type="xsd:dateTime"/>
              <xsd:element name="recordCount" nillable="false" type="xsd:int"/>
              <xsd:element name="sortBetsBy" type="types:BetsOrderByEnum"/>
              <xsd:element name="startRecord" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfMarketTypeEnum">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="MarketTypeEnum" nillable="true" type="types:MarketTypeEnum"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfInt">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="int" nillable="true"  type="xsd:int"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="GetAccountStatementResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetAccountStatementErrorEnum"/>
              <xsd:element name="items" nillable="true" type="types:ArrayOfAccountStatementItem"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="totalRecordCount" nillable="false" type="xsd:int"/>              
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetAccountStatementErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_START_RECORD"/>
          <xsd:enumeration value="INVALID_RECORD_COUNT"/>
          <xsd:enumeration value="INVALID_END_DATE"/>
          <xsd:enumeration value="INVALID_START_DATE"/>
          <xsd:enumeration value="NO_RESULTS"/>
          <xsd:enumeration value="API_ERROR"/>
          <xsd:enumeration value="INVALID_LOCALE_DEFAULTING_TO_ENGLISH"/>          
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="AccountStatementItem">
        <xsd:sequence>
          <xsd:element name="accountBalance" nillable="false" type="xsd:double"/>
          <xsd:element name="amount"  nillable="false" type="xsd:double"/>
          <xsd:element name="avgPrice"  nillable="false" type="xsd:double"/>
          <xsd:element name="betId" type="xsd:long"/>
          <xsd:element name="betSize"  nillable="false" type="xsd:double"/>
          <xsd:element name="betType" type="types:BetTypeEnum"/>
          <xsd:element name="betCategoryType" type="types:BetCategoryTypeEnum"/>
          <xsd:element name="commissionRate" nillable="true" type="xsd:string"/>
          <xsd:element name="eventId" nillable="false" type="xsd:int"/>
          <xsd:element name="eventTypeId" nillable="false" type="xsd:int"/>
          <xsd:element name="fullMarketName" nillable="true" type="xsd:string"/>
          <xsd:element name="grossBetAmount" nillable="false" type="xsd:double"/>
          <xsd:element name="marketName" nillable="true" type="xsd:string"/>
          <xsd:element name="marketType" type="types:MarketTypeEnum"/>
          <xsd:element name="placedDate" type="xsd:dateTime"/>
          <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
          <xsd:element name="selectionName" nillable="true" type="xsd:string"/>
          <xsd:element name="settledDate" type="xsd:dateTime"/>
          <xsd:element name="startDate" type="xsd:dateTime"/>
          <xsd:element name="transactionType" type="types:AccountStatementEnum"/>
          <xsd:element name="transactionId" type="xsd:long"/>          
          <xsd:element name="winLose" type="types:AccountStatementEnum"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="AccountStatementEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="RESULT_WON"/>
          <xsd:enumeration value="RESULT_LOST"/>
          <xsd:enumeration value="RESULT_ERR"/>
          <xsd:enumeration value="RESULT_FIX"/>
          <xsd:enumeration value="RESULT_NOT_APPLICABLE"/>
          <xsd:enumeration value="ACCOUNT_CREDIT"/>
          <xsd:enumeration value="ACCOUNT_DEBIT"/>
          <xsd:enumeration value="COMMISSION_REVERSAL"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ArrayOfAccountStatementItem">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="AccountStatementItem" nillable="true" type="types:AccountStatementItem"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetAccountStatementReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="endDate" type="xsd:dateTime"/>
              <xsd:element name="itemsIncluded" type="types:AccountStatementIncludeEnum"/>
              <xsd:element name="ignoreAutoTransfers" nillable="false" type="xsd:boolean"/>
              <xsd:element name="recordCount" nillable="false" type="xsd:int"/>
              <xsd:element name="startDate" type="xsd:dateTime"/>
              <xsd:element name="startRecord" nillable="false" type="xsd:int"/>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>              
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="AccountStatementIncludeEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="ALL"/>
          <xsd:enumeration value="EXCHANGE"/>
          <xsd:enumeration value="POKER_ROOM"/>
          <xsd:enumeration value="DEPOSITS_WITHDRAWALS"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="GetMarketProfitAndLossResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="annotations" nillable="true" type="types:ArrayOfProfitAndLoss"/>
              <xsd:element name="commissionApplied" nillable="false" type="xsd:double"/>
              <xsd:element name="currencyCode" nillable="true" type="xsd:string"/>
              <xsd:element name="errorCode" type="types:GetMarketProfitAndLossErrorEnum"/>
              <xsd:element name="includesSettledBets" nillable="false" type="xsd:boolean"/>
              <xsd:element name="includesBspBets" nillable="false" type="xsd:boolean"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
              <xsd:element name="marketName" nillable="true" type="xsd:string"/>
              <xsd:element name="marketStatus" type="types:MarketStatusEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="unit" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="ProfitAndLoss">
        <xsd:sequence>
          <xsd:element name="futureIfWin" nillable="false" type="xsd:double"/>
          <xsd:element name="ifWin" nillable="false" type="xsd:double"/>
          <xsd:element name="selectionId" nillable="false" type="xsd:int"/>
          <xsd:element name="selectionName" nillable="true" type="xsd:string"/>
          <xsd:element name="worstcaseIfWin" nillable="false" type="xsd:double"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfProfitAndLoss">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="ProfitAndLoss" nillable="true" type="types:ProfitAndLoss"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="GetMarketProfitAndLossErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="INVALID_MARKET"/>
          <xsd:enumeration value="UNSUPPORTED_MARKET_TYPE"/>
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="MARKET_CLOSED"/>
          <xsd:enumeration value="INVALID_LOCALE_DEFAULTING_TO_ENGLISH"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="GetMarketProfitAndLossReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
              <xsd:element name="includeSettledBets" nillable="false" type="xsd:boolean"/>
              <xsd:element name="includeBspBets" nillable="false" type="xsd:boolean"/>
              <xsd:element name="marketID" nillable="false" type="xsd:int"/>
              <xsd:element name="netOfCommission" nillable="false" type="xsd:boolean"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetBetResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="bet" nillable="true" type="types:Bet"/>
              <xsd:element name="errorCode" type="types:GetBetErrorEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="GetBetErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="MARKET_TYPE_NOT_SUPPORTED"/>
          <xsd:enumeration value="BET_ID_INVALID"/>
          <xsd:enumeration value="NO_RESULTS"/>
          <xsd:enumeration value="API_ERROR"/>
          <xsd:enumeration value="INVALID_LOCALE_DEFAULTING_TO_ENGLISH"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="GetBetReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="betId" nillable="false" type="xsd:long"/>
              <xsd:element name="locale" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>


      <xsd:complexType name="GetBetLiteResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="betLite" nillable="true" type="types:BetLite"/>
              <xsd:element name="errorCode" type="types:GetBetErrorEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="BetLite">
        <xsd:sequence>
          <xsd:element name="betId" type="xsd:long"/>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="matchedSize" nillable="false" type="xsd:double"/>
          <xsd:element name="remainingSize" nillable="false" type="xsd:double"/>
          <xsd:element name="betStatus" type="types:BetStatusEnum"/>
          <xsd:element name="betCategoryType" type="types:BetCategoryTypeEnum"/>
          <xsd:element name="betPersistenceType" type="types:BetPersistenceTypeEnum"/>
          <xsd:element name="bspLiability" nillable="true" type="xsd:double"/>                    
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfBetLite">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="BetLite" nillable="true" type="types:BetLite"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetBetLiteReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="betId" nillable="false" type="xsd:long"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetBetMatchesLiteReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="betId" nillable="false" type="xsd:long"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetBetMatchesLiteResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="matchLites" nillable="true" type="types:ArrayOfMatchLite"/>
              <xsd:element name="errorCode" type="types:GetBetErrorEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="MatchLite">
        <xsd:sequence>
          <xsd:element name="betStatus" type="types:BetStatusEnum"/>
          <xsd:element name="matchedDate" type="xsd:dateTime"/>
          <xsd:element name="priceMatched" nillable="false" type="xsd:double"/>
          <xsd:element name="sizeMatched" nillable="false" type="xsd:double"/>
          <xsd:element name="transactionId" type="xsd:long"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfMatchLite">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="MatchLite" nillable="true" type="types:MatchLite"/>
        </xsd:sequence>
      </xsd:complexType>
      

      <xsd:complexType name="GetCurrentBetsLiteResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="betLites" nillable="true" type="types:ArrayOfBetLite"/>
              <xsd:element name="errorCode" type="types:GetCurrentBetsErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="totalRecordCount" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetCurrentBetsLiteReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="betStatus" type="types:BetStatusEnum"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
              <xsd:element name="orderBy" type="types:BetsOrderByEnum"/>
              <xsd:element name="recordCount" nillable="false" type="xsd:int"/>
              <xsd:element name="startRecord" nillable="false" type="xsd:int"/>
              <xsd:element name="noTotalRecordCount" nillable="false" type="xsd:boolean"/>              
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="MUBetLite">
        <xsd:sequence>
          <xsd:element name="betId" type="xsd:long"/>
          <xsd:element name="transactionId" type="xsd:long"/>
          <xsd:element name="marketId" nillable="false" type="xsd:int"/>
          <xsd:element name="size" nillable="false" type="xsd:double"/>
          <xsd:element name="betStatus" type="types:BetStatusEnum"/>
          <xsd:element name="betCategoryType" type="types:BetCategoryTypeEnum"/>
          <xsd:element name="betPersistenceType" type="types:BetPersistenceTypeEnum"/>
          <xsd:element name="bspLiability" nillable="true" type="xsd:double"/>                    
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfMUBetLite">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" minOccurs="0"
            name="MUBetLite" nillable="true" type="types:MUBetLite"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetMUBetsLiteResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="betLites" nillable="true" type="types:ArrayOfMUBetLite"/>
              <xsd:element name="errorCode" type="types:GetMUBetsErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="totalRecordCount" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetMUBetsLiteReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="betStatus" type="types:BetStatusEnum"/>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
              <xsd:element name="betIds" nillable="true" type="types:ArrayOfBetId"/>              
              <xsd:element name="orderBy" type="types:BetsOrderByEnum"/>
              <xsd:element name="sortOrder" type="types:SortOrderEnum"/>
              <xsd:element name="recordCount" nillable="false" type="xsd:int"/>
              <xsd:element name="startRecord" nillable="false" type="xsd:int"/>
              <xsd:element name="matchedSince" nillable="true" type="xsd:dateTime"/>
              <xsd:element name="excludeLastSecond" nillable="false" type="xsd:boolean"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetMarketInfoResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" type="types:GetMarketErrorEnum"/>
              <xsd:element name="marketLite" nillable="true" type="types:MarketLite"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="MarketLite">
        <xsd:sequence>
          <xsd:element name="marketStatus" type="types:MarketStatusEnum"/>
          <xsd:element name="marketSuspendTime" type="xsd:dateTime"/>
          <xsd:element name="marketTime" type="xsd:dateTime"/>
          <xsd:element name="numberOfRunners" nillable="false" type="xsd:int"/>
          <xsd:element name="delay" nillable="false" type="xsd:int"/>
          <xsd:element name="reconciled" nillable="false" type="xsd:boolean"/>
          <xsd:element name="openForBspBetting" nillable="false" type="xsd:boolean"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="GetMarketInfoReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="marketId" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>

      <xsd:complexType name="HandicapLine">
        <xsd:complexContent>
          <xsd:extension base="types:ProfitAndLoss">
            <xsd:sequence>
              <xsd:element name="from" nillable="false" type="xsd:double"/>
              <xsd:element name="to" nillable="false" type="xsd:double"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="MultiWinnerOddsLine">
        <xsd:complexContent>
          <xsd:extension base="types:ProfitAndLoss">
            <xsd:sequence>
              <xsd:element name="ifLoss" nillable="false" type="xsd:double"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
    </xsd:schema>

    
    <xsd:schema elementFormDefault="qualified" targetNamespace="http://www.betfair.com/publicapi/v5/BFExchangeService/">
      <xsd:import namespace="http://www.betfair.com/publicapi/types/exchange/v5/"/>
      
      <xsd:element name="getAccountFunds">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetAccountFundsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getAccountFundsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetAccountFundsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="cancelBets">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:CancelBetsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="cancelBetsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:CancelBetsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      
      <xsd:element name="cancelBetsByMarket">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:CancelBetsByMarketReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="cancelBetsByMarketResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:CancelBetsByMarketResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>      
      
         <xsd:element name="heartbeat">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:HeartbeatReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="heartbeatResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:HeartbeatResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      
      <xsd:element name="getSilks">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetSilksReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getSilksResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetSilksResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      
      <xsd:element name="getSilksV2">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetSilksV2Req"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getSilksV2Response">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetSilksV2Resp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="updateBets">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:UpdateBetsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="updateBetsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:UpdateBetsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="placeBets">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:PlaceBetsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="placeBetsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:PlaceBetsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getCoupon">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetCouponReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getCouponResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetCouponResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getMarket">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetMarketReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
        <xsd:element name="getMarketInfo">
              <xsd:complexType>
                <xsd:sequence>
                  <xsd:element name="request" type="types:GetMarketInfoReq"/>
                </xsd:sequence>
              </xsd:complexType>
            </xsd:element>
            <xsd:element name="getMarketInfoResponse">
              <xsd:complexType>
                <xsd:sequence>
                  <xsd:element name="Result" nillable="true" type="types:GetMarketInfoResp"/>
                </xsd:sequence>
              </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMarketResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetMarketResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMarketPrices">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetMarketPricesReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMarketPricesResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetMarketPricesResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getCompleteMarketPricesCompressed">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetCompleteMarketPricesCompressedReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getCompleteMarketPricesCompressedResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetCompleteMarketPricesCompressedResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getMarketTradedVolumeCompressed">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetMarketTradedVolumeCompressedReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMarketTradedVolumeCompressedResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetMarketTradedVolumeCompressedResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getMarketPricesCompressed">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetMarketPricesCompressedReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMarketPricesCompressedResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetMarketPricesCompressedResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      

      <xsd:element name="getAllMarkets">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetAllMarketsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getAllMarketsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetAllMarketsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getInPlayMarkets">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetInPlayMarketsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getInPlayMarketsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetInPlayMarketsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getPrivateMarkets">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetPrivateMarketsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getPrivateMarketsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetPrivateMarketsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>      

      <xsd:element name="getCurrentBets">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetCurrentBetsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getCurrentBetsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetCurrentBetsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

     <xsd:element name="getCurrentBetsLite">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetCurrentBetsLiteReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getCurrentBetsLiteResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetCurrentBetsLiteResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getMUBets">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetMUBetsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMUBetsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetMUBetsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

     <xsd:element name="getMUBetsLite">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetMUBetsLiteReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMUBetsLiteResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetMUBetsLiteResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getDetailAvailableMktDepth">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetDetailedAvailableMktDepthReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getDetailAvailableMktDepthResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetDetailedAvailableMktDepthResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMarketTradedVolume">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetMarketTradedVolumeReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMarketTradedVolumeResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetMarketTradedVolumeResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getBetHistory">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetBetHistoryReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getBetHistoryResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetBetHistoryResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getAccountStatement">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="req" type="types:GetAccountStatementReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getAccountStatementResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetAccountStatementResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMarketProfitAndLoss">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetMarketProfitAndLossReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getMarketProfitAndLossResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetMarketProfitAndLossResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getBet">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetBetReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getBetResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetBetResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

   <xsd:element name="getBetLite">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetBetLiteReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getBetLiteResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetBetLiteResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getBetMatchesLite">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetBetMatchesLiteReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getBetMatchesLiteResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetBetMatchesLiteResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

    </xsd:schema>
 
  </wsdl:types>

  <wsdl:message name="getSilksIn">
    <wsdl:part element="tns:getSilks" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getSilksOut">
    <wsdl:part element="tns:getSilksResponse" name="parameters"/>
  </wsdl:message>
  
  <wsdl:message name="getSilksV2In">
    <wsdl:part element="tns:getSilksV2" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getSilksV2Out">
    <wsdl:part element="tns:getSilksV2Response" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getAccountFundsIn">
    <wsdl:part element="tns:getAccountFunds" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getAccountFundsOut">
    <wsdl:part element="tns:getAccountFundsResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="cancelBetsIn">
    <wsdl:part element="tns:cancelBets" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="cancelBetsOut">
    <wsdl:part element="tns:cancelBetsResponse" name="parameters"/>
  </wsdl:message>
   <wsdl:message name="cancelBetsByMarketIn">
      <wsdl:part element="tns:cancelBetsByMarket" name="parameters"/>
    </wsdl:message>
    <wsdl:message name="cancelBetsByMarketOut">
      <wsdl:part element="tns:cancelBetsByMarketResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="updateBetsIn">
    <wsdl:part element="tns:updateBets" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="updateBetsOut">
    <wsdl:part element="tns:updateBetsResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="placeBetsIn">
    <wsdl:part element="tns:placeBets" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="placeBetsOut">
    <wsdl:part element="tns:placeBetsResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketIn">
    <wsdl:part element="tns:getMarket" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketOut">
    <wsdl:part element="tns:getMarketResponse" name="parameters"/>
  </wsdl:message>
   <wsdl:message name="getMarketInfoIn">
      <wsdl:part element="tns:getMarketInfo" name="parameters"/>
    </wsdl:message>
    <wsdl:message name="getMarketInfoOut">
      <wsdl:part element="tns:getMarketInfoResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketPricesIn">
    <wsdl:part element="tns:getMarketPrices" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketPricesOut">
    <wsdl:part element="tns:getMarketPricesResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getCompleteMarketPricesCompressedIn">
    <wsdl:part element="tns:getCompleteMarketPricesCompressed" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getCompleteMarketPricesCompressedOut">
    <wsdl:part element="tns:getCompleteMarketPricesCompressedResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getMarketTradedVolumeCompressedIn">
    <wsdl:part element="tns:getMarketTradedVolumeCompressed" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketTradedVolumeCompressedOut">
    <wsdl:part element="tns:getMarketTradedVolumeCompressedResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getMarketPricesCompressedIn">
    <wsdl:part element="tns:getMarketPricesCompressed" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketPricesCompressedOut">
    <wsdl:part element="tns:getMarketPricesCompressedResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getAllMarketsIn">
    <wsdl:part element="tns:getAllMarkets" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getAllMarketsOut">
    <wsdl:part element="tns:getAllMarketsResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getInPlayMarketsIn">
    <wsdl:part element="tns:getInPlayMarkets" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getInPlayMarketsOut">
    <wsdl:part element="tns:getInPlayMarketsResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getPrivateMarketsIn">
    <wsdl:part element="tns:getPrivateMarkets" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getPrivateMarketsOut">
    <wsdl:part element="tns:getPrivateMarketsResponse" name="parameters"/>
  </wsdl:message>  
  
  <wsdl:message name="getCurrentBetsIn">
    <wsdl:part element="tns:getCurrentBets" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getCurrentBetsOut">
    <wsdl:part element="tns:getCurrentBetsResponse" name="parameters"/>
  </wsdl:message>
  
    <wsdl:message name="getCurrentBetsLiteIn">
      <wsdl:part element="tns:getCurrentBetsLite" name="parameters"/>
    </wsdl:message>
    <wsdl:message name="getCurrentBetsLiteOut">
      <wsdl:part element="tns:getCurrentBetsLiteResponse" name="parameters"/>
    </wsdl:message>


  <wsdl:message name="getMUBetsIn">
    <wsdl:part element="tns:getMUBets" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMUBetsOut">
    <wsdl:part element="tns:getMUBetsResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getMUBetsLiteIn">
    <wsdl:part element="tns:getMUBetsLite" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMUBetsLiteOut">
    <wsdl:part element="tns:getMUBetsLiteResponse" name="parameters"/>
  </wsdl:message>
  
  <wsdl:message name="getDetailAvailableMktDepthIn">
    <wsdl:part element="tns:getDetailAvailableMktDepth" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getDetailAvailableMktDepthOut">
    <wsdl:part element="tns:getDetailAvailableMktDepthResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketTradedVolumeIn">
    <wsdl:part element="tns:getMarketTradedVolume" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketTradedVolumeOut">
    <wsdl:part element="tns:getMarketTradedVolumeResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getBetHistoryIn">
    <wsdl:part element="tns:getBetHistory" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getBetHistoryOut">
    <wsdl:part element="tns:getBetHistoryResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getAccountStatementIn">
    <wsdl:part element="tns:getAccountStatement" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getAccountStatementOut">
    <wsdl:part element="tns:getAccountStatementResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketProfitAndLossIn">
    <wsdl:part element="tns:getMarketProfitAndLoss" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getMarketProfitAndLossOut">
    <wsdl:part element="tns:getMarketProfitAndLossResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getBetIn">
    <wsdl:part element="tns:getBet" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getBetOut">
    <wsdl:part element="tns:getBetResponse" name="parameters"/>
  </wsdl:message>
  
    <wsdl:message name="heartbeatIn">
    <wsdl:part element="tns:heartbeat" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="heartbeatOut">
    <wsdl:part element="tns:heartbeatResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getCouponIn">
    <wsdl:part element="tns:getCoupon" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getCouponOut">
    <wsdl:part element="tns:getCouponResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getBetLiteIn">
    <wsdl:part element="tns:getBetLite" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getBetLiteOut">
    <wsdl:part element="tns:getBetLiteResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getBetMatchesLiteIn">
    <wsdl:part element="tns:getBetMatchesLite" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getBetMatchesLiteOut">
    <wsdl:part element="tns:getBetMatchesLiteResponse" name="parameters"/>
  </wsdl:message>
  <wsdl:portType name="BFExchangeService">
  
	<wsdl:operation name="getSilks">
      <wsdl:input message="tns:getSilksIn" name="getSilksIn"/>
      <wsdl:output message="tns:getSilksOut" name="getSilksOut"/>
    </wsdl:operation>

	<wsdl:operation name="getSilksV2">
      <wsdl:input message="tns:getSilksV2In" name="getSilksV2In"/>
      <wsdl:output message="tns:getSilksV2Out" name="getSilksV2Out"/>
    </wsdl:operation>

    <wsdl:operation name="getAccountFunds">
      <wsdl:input message="tns:getAccountFundsIn" name="getAccountFundsIn"/>
      <wsdl:output message="tns:getAccountFundsOut" name="getAccountFundsOut"/>
    </wsdl:operation>


  <wsdl:operation name="heartbeat">
      <wsdl:input message="tns:heartbeatIn" name="heartbeatIn"/>
      <wsdl:output message="tns:heartbeatOut" name="heartbeatOut"/>
    </wsdl:operation>


    <wsdl:operation name="cancelBets">
      <wsdl:input message="tns:cancelBetsIn" name="cancelBetsIn"/>
      <wsdl:output message="tns:cancelBetsOut" name="cancelBetsOut"/>
    </wsdl:operation>
  <wsdl:operation name="cancelBetsByMarket">
      <wsdl:input message="tns:cancelBetsByMarketIn" name="cancelBetsByMarketIn"/>
      <wsdl:output message="tns:cancelBetsByMarketOut" name="cancelBetsByMarketOut"/>
    </wsdl:operation>    
    <wsdl:operation name="updateBets">
      <wsdl:input message="tns:updateBetsIn" name="updateBetsIn"/>
      <wsdl:output message="tns:updateBetsOut" name="updateBetsOut"/>
    </wsdl:operation>
    <wsdl:operation name="placeBets">
      <wsdl:input message="tns:placeBetsIn" name="placeBetsIn"/>
      <wsdl:output message="tns:placeBetsOut" name="placeBetsOut"/>
    </wsdl:operation>
    <wsdl:operation name="getMarket">
      <wsdl:input message="tns:getMarketIn" name="getMarketIn"/>
      <wsdl:output message="tns:getMarketOut" name="getMarketOut"/>
    </wsdl:operation>
       <wsdl:operation name="getMarketInfo">
          <wsdl:input message="tns:getMarketInfoIn" name="getMarketInfoIn"/>
          <wsdl:output message="tns:getMarketInfoOut" name="getMarketInfoOut"/>
        </wsdl:operation>

    <wsdl:operation name="getMarketPrices">
      <wsdl:input message="tns:getMarketPricesIn" name="getMarketPricesIn"/>
      <wsdl:output message="tns:getMarketPricesOut" name="getMarketPricesOut"/>
    </wsdl:operation>
    <wsdl:operation name="getCompleteMarketPricesCompressed">
      <wsdl:input message="tns:getCompleteMarketPricesCompressedIn" name="getCompleteMarketPricesCompressedIn"/>
      <wsdl:output message="tns:getCompleteMarketPricesCompressedOut" name="getCompleteMarketPricesCompressedOut"/>
    </wsdl:operation>

    <wsdl:operation name="getMarketTradedVolumeCompressed">
      <wsdl:input message="tns:getMarketTradedVolumeCompressedIn" name="getMarketTradedVolumeCompressedIn"/>
      <wsdl:output message="tns:getMarketTradedVolumeCompressedOut" name="getMarketTradedVolumeCompressedOut"/>
    </wsdl:operation>

    <wsdl:operation name="getMarketPricesCompressed">
      <wsdl:input message="tns:getMarketPricesCompressedIn" name="getMarketPricesCompressedIn"/>
      <wsdl:output message="tns:getMarketPricesCompressedOut" name="getMarketPricesCompressedOut"/>
    </wsdl:operation>
    
      <wsdl:operation name="getAllMarkets">
          <wsdl:input message="tns:getAllMarketsIn" name="getAllMarketsIn"/>
          <wsdl:output message="tns:getAllMarketsOut" name="getAllMarketsOut"/>
        </wsdl:operation>
    
        <wsdl:operation name="getInPlayMarkets">
          <wsdl:input message="tns:getInPlayMarketsIn" name="getInPlayMarketsIn"/>
          <wsdl:output message="tns:getInPlayMarketsOut" name="getInPlayMarketsOut"/>
        </wsdl:operation>
    
        <wsdl:operation name="getPrivateMarkets">
          <wsdl:input message="tns:getPrivateMarketsIn" name="getPrivateMarketsIn"/>
          <wsdl:output message="tns:getPrivateMarketsOut" name="getPrivateMarketsOut"/>
    </wsdl:operation>
    
    <wsdl:operation name="getCurrentBets">
      <wsdl:input message="tns:getCurrentBetsIn" name="getCurrentBetsIn"/>
      <wsdl:output message="tns:getCurrentBetsOut" name="getCurrentBetsOut"/>
    </wsdl:operation>

  <wsdl:operation name="getCurrentBetsLite">
      <wsdl:input message="tns:getCurrentBetsLiteIn" name="getCurrentBetsLiteIn"/>
      <wsdl:output message="tns:getCurrentBetsLiteOut" name="getCurrentBetsLiteOut"/>
    </wsdl:operation>


    <wsdl:operation name="getMUBets">
      <wsdl:input message="tns:getMUBetsIn" name="getMUBetsIn"/>
      <wsdl:output message="tns:getMUBetsOut" name="getMUBetsOut"/>
    </wsdl:operation>

    <wsdl:operation name="getMUBetsLite">
      <wsdl:input message="tns:getMUBetsLiteIn" name="getMUBetsLiteIn"/>
      <wsdl:output message="tns:getMUBetsLiteOut" name="getMUBetsLiteOut"/>
    </wsdl:operation>


    <wsdl:operation name="getDetailAvailableMktDepth">
      <wsdl:input message="tns:getDetailAvailableMktDepthIn" name="getDetailAvailableMktDepthIn"/>
      <wsdl:output message="tns:getDetailAvailableMktDepthOut" name="getDetailAvailableMktDepthOut"/>
    </wsdl:operation>
    <wsdl:operation name="getMarketTradedVolume">
      <wsdl:input message="tns:getMarketTradedVolumeIn" name="getMarketTradedVolumeIn"/>
      <wsdl:output message="tns:getMarketTradedVolumeOut" name="getMarketTradedVolumeOut"/>
    </wsdl:operation>
    <wsdl:operation name="getBetHistory">
      <wsdl:input message="tns:getBetHistoryIn" name="getBetHistoryIn"/>
      <wsdl:output message="tns:getBetHistoryOut" name="getBetHistoryOut"/>
    </wsdl:operation>
    <wsdl:operation name="getAccountStatement">
      <wsdl:input message="tns:getAccountStatementIn" name="getAccountStatementIn"/>
      <wsdl:output message="tns:getAccountStatementOut" name="getAccountStatementOut"/>
    </wsdl:operation>
    <wsdl:operation name="getMarketProfitAndLoss">
      <wsdl:input message="tns:getMarketProfitAndLossIn" name="getMarketProfitAndLossIn"/>
      <wsdl:output message="tns:getMarketProfitAndLossOut" name="getMarketProfitAndLossOut"/>
    </wsdl:operation>
    <wsdl:operation name="getBet">
      <wsdl:input message="tns:getBetIn" name="getBetIn"/>
      <wsdl:output message="tns:getBetOut" name="getBetOut"/>
    </wsdl:operation>

    <wsdl:operation name="getCoupon">
      <wsdl:input message="tns:getCouponIn" name="getCouponIn"/>
      <wsdl:output message="tns:getCouponOut" name="getCouponOut"/>
    </wsdl:operation>

    <wsdl:operation name="getBetLite">
      <wsdl:input message="tns:getBetLiteIn" name="getBetLiteIn"/>
      <wsdl:output message="tns:getBetLiteOut" name="getBetLiteOut"/>
    </wsdl:operation>
    <wsdl:operation name="getBetMatchesLite">
      <wsdl:input message="tns:getBetMatchesLiteIn" name="getBetMatchesLiteIn"/>
      <wsdl:output message="tns:getBetMatchesLiteOut" name="getBetMatchesLiteOut"/>
    </wsdl:operation>

  </wsdl:portType>
  <wsdl:binding name="BFExchangeService" type="tns:BFExchangeService">
    <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
    
    <wsdl:operation name="getAccountFunds">
      <soap:operation soapAction="getAccountFunds" style="document"/>
      <wsdl:input name="getAccountFundsIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getAccountFundsOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="cancelBets">
      <soap:operation soapAction="cancelBets" style="document"/>
      <wsdl:input name="cancelBetsIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="cancelBetsOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    
       <wsdl:operation name="cancelBetsByMarket">
          <soap:operation soapAction="cancelBetsByMarket" style="document"/>
          <wsdl:input name="cancelBetsByMarketIn">
            <soap:body use="literal"/>
          </wsdl:input>
          <wsdl:output name="cancelBetsByMarketOut">
            <soap:body use="literal"/>
          </wsdl:output>
    </wsdl:operation>
    
    <wsdl:operation name="updateBets">
      <soap:operation soapAction="updateBets" style="document"/>
      <wsdl:input name="updateBetsIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="updateBetsOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="placeBets">
      <soap:operation soapAction="placeBets" style="document"/>
      <wsdl:input name="placeBetsIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="placeBetsOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getMarket">
      <soap:operation soapAction="getMarket" style="document"/>
      <wsdl:input name="getMarketIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getMarketOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    
        <wsdl:operation name="getMarketInfo">
          <soap:operation soapAction="getMarketInfo" style="document"/>
          <wsdl:input name="getMarketInfoIn">
            <soap:body use="literal"/>
          </wsdl:input>
          <wsdl:output name="getMarketInfoOut">
            <soap:body use="literal"/>
          </wsdl:output>
        </wsdl:operation>

    <wsdl:operation name="getMarketPrices">
      <soap:operation soapAction="getMarketPrices" style="document"/>
      <wsdl:input name="getMarketPricesIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getMarketPricesOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getCompleteMarketPricesCompressed">
      <soap:operation soapAction="getCompleteMarketPricesCompressed" style="document"/>
      <wsdl:input name="getCompleteMarketPricesCompressedIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getCompleteMarketPricesCompressedOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="getMarketTradedVolumeCompressed">
      <soap:operation soapAction="getMarketTradedVolumeCompressed" style="document"/>
      <wsdl:input name="getMarketTradedVolumeCompressedIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getMarketTradedVolumeCompressedOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="getMarketPricesCompressed">
      <soap:operation soapAction="getMarketPricesCompressed" style="document"/>
      <wsdl:input name="getMarketPricesCompressedIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getMarketPricesCompressedOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    
    
        <wsdl:operation name="getAllMarkets">
          <soap:operation soapAction="getAllMarkets" style="document"/>
          <wsdl:input name="getAllMarketsIn">
            <soap:body use="literal"/>
          </wsdl:input>
          <wsdl:output name="getAllMarketsOut">
            <soap:body use="literal"/>
          </wsdl:output>
        </wsdl:operation>
    
        <wsdl:operation name="getInPlayMarkets">
          <soap:operation soapAction="getInPlayMarkets" style="document"/>
          <wsdl:input name="getInPlayMarketsIn">
            <soap:body use="literal"/>
          </wsdl:input>
          <wsdl:output name="getInPlayMarketsOut">
            <soap:body use="literal"/>
          </wsdl:output>
        </wsdl:operation>
    
        <wsdl:operation name="getPrivateMarkets">
          <soap:operation soapAction="getPrivateMarkets" style="document"/>
          <wsdl:input name="getPrivateMarketsIn">
            <soap:body use="literal"/>
          </wsdl:input>
          <wsdl:output name="getPrivateMarketsOut">
            <soap:body use="literal"/>
          </wsdl:output>
        </wsdl:operation>

    <wsdl:operation name="getCurrentBets">
      <soap:operation soapAction="getCurrentBets" style="document"/>
      <wsdl:input name="getCurrentBetsIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getCurrentBetsOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="getCoupon">
      <soap:operation soapAction="getCoupon" style="document"/>
      <wsdl:input name="getCouponIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getCouponOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    
       <wsdl:operation name="getCurrentBetsLite">
          <soap:operation soapAction="getCurrentBetsLite" style="document"/>
          <wsdl:input name="getCurrentBetsLiteIn">
           <soap:body use="literal"/>
          </wsdl:input>
         <wsdl:output name="getCurrentBetsLiteOut">
           <soap:body use="literal"/>
          </wsdl:output>
        </wsdl:operation>


    <wsdl:operation name="getMUBets">
      <soap:operation soapAction="getMUBets" style="document"/>
      <wsdl:input name="getMUBetsIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getMUBetsOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    
        <wsdl:operation name="getMUBetsLite">
          <soap:operation soapAction="getMUBetsLite" style="document"/>
          <wsdl:input name="getMUBetsLiteIn">
            <soap:body use="literal"/>
          </wsdl:input>
          <wsdl:output name="getMUBetsLiteOut">
            <soap:body use="literal"/>
          </wsdl:output>
        </wsdl:operation>

 
    <wsdl:operation name="getDetailAvailableMktDepth">
      <soap:operation soapAction="getDetailAvailableMktDepth" style="document"/>
      <wsdl:input name="getDetailAvailableMktDepthIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getDetailAvailableMktDepthOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getMarketTradedVolume">
      <soap:operation soapAction="getMarketTradedVolume" style="document"/>
      <wsdl:input name="getMarketTradedVolumeIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getMarketTradedVolumeOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getBetHistory">
      <soap:operation soapAction="getBetHistory" style="document"/>
      <wsdl:input name="getBetHistoryIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getBetHistoryOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getAccountStatement">
      <soap:operation soapAction="getAccountStatement" style="document"/>
      <wsdl:input name="getAccountStatementIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getAccountStatementOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getMarketProfitAndLoss">
      <soap:operation soapAction="getMarketProfitAndLoss" style="document"/>
      <wsdl:input name="getMarketProfitAndLossIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getMarketProfitAndLossOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getBet">
      <soap:operation soapAction="getBet" style="document"/>
      <wsdl:input name="getBetIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getBetOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getBetLite">
      <soap:operation soapAction="getBetLite" style="document"/>
      <wsdl:input name="getBetLiteIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getBetLiteOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="getBetMatchesLite">
      <soap:operation soapAction="getBetMatchesLite" style="document"/>
      <wsdl:input name="getBetMatchesLiteIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getBetMatchesLiteOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
  
  
    <wsdl:operation name="getSilks">
      <soap:operation soapAction="getSilks" style="document"/>
      <wsdl:input name="getSilksIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getSilksOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>  

    <wsdl:operation name="getSilksV2">
      <soap:operation soapAction="getSilksV2" style="document"/>
      <wsdl:input name="getSilksV2In">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getSilksV2Out">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>  
        
    <wsdl:operation name="heartbeat">
      <soap:operation soapAction="heartbeat" style="document"/>
      <wsdl:input name="heartbeatIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="heartbeatOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    
  </wsdl:binding>
  <wsdl:service name="BFExchangeService">
    <wsdl:port binding="tns:BFExchangeService" name="BFExchangeService">
      <soap:address location="https://api-au.betfair.com/exchange/v5/BFExchangeService"/>
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>
'''

BFVendorService = '''
<?xml version="1.0" encoding="UTF-8"?>

<!--

Copyright 2003-2004 The Sporting Exchange Limited. All rights reserved. 
The presentation, distribution or other dissemination of the information contained herein by The Sporting Exchange Limited (Betfair) is not a license, either expressly or impliedly, to any intellectual property owned or controlled by Betfair.
Save as provided by statute and to the fullest extent permitted by law, the following provisions set out the entire liability of Betfair (including any liability for the acts and omissions of its employees, agents and sub-contractors) to the User in respect of the use of its WSDL file whether in contract, tort, statute, equity or otherwise: 
(a)     The User acknowledges and agrees that (except as expressly provided in this Agreement) the WSDL is provided "AS IS" without warranties of any kind (whether express or implied);
(b)    All conditions, warranties, terms and undertakings (whether express or implied, statutory or otherwise relating to the delivery, performance, quality, uninterrupted use, fitness for purpose, occurrence or reliability of the WSDL are hereby excluded to the fullest extent permitted by law; and 
(c)     Betfair shall not be liable to the User for loss of profit (whether direct or indirect), loss of contracts or goodwill, lost advertising, loss of data or any type of special, indirect, consequential or economic loss (including loss or damage suffered by the User as a result of an action brought by a third party) even if such loss was reasonably foreseeable or Betfair had been advised of the possibility of the User incurring such loss.
No exclusion or limitation set out in this Agreement shall apply in the case of fraud or fraudulent concealment, death or personal injury resulting from the negligence of either party or any of its employees, agents or sub-contractors; and/or any breach of the obligations implied by (as appropriate) section 12 of the Sale of Goods Act 1979, section 2 of the Supply of Goods and Services Act 1982 or section 8 of the Supply of Goods (Implied Terms) Act 1973.

-->

<wsdl:definitions name="VendorService"
	xmlns:http="http://schemas.xmlsoap.org/wsdl/http/" 
	xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" 
	xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
	xmlns:types="http://www.betfair.com/adminapi/types/v2/"
	xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" 
	xmlns:tns="http://www.betfair.com/adminapi/v2/VendorService/" 
	xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/" 
	xmlns:mime="http://schemas.xmlsoap.org/wsdl/mime/" 
	targetNamespace="http://www.betfair.com/adminapi/v2/VendorService/" 
	xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">
  <wsdl:types>
    <xsd:schema targetNamespace="http://www.betfair.com/adminapi/types/v2/">
      <xsd:import namespace="http://schemas.xmlsoap.org/soap/encoding/"/>


      <xsd:complexType name="SetAccessRequestReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
          <xsd:sequence>
            <xsd:element name="accessRequestToken" nillable="false" type="xsd:string"/>
          </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="SetAccessRequestResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
                <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
                <xsd:element name="vendorClientId" nillable="false" type="xsd:int"/>
                <xsd:element name="vendorSoftwareName" nillable="false" type="xsd:string"/>
                <xsd:element name="expiryDate" nillable="false" type="xsd:dateTime"/>
                <xsd:element name="errorCode" type="types:SetAccessRequestErrorEnum"/>
                <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="SetAccessRequestErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_ACCESS_REQUEST_TOKEN"/>
          <xsd:enumeration value="REQUEST_ALREADY_DONE"/>
          <xsd:enumeration value="REQUEST_EXPIRED"/>
          <xsd:enumeration value="REQUEST_CANCELLED"/>
          <xsd:enumeration value='VENDOR_SOFTWARE_INVALID'/>
          <xsd:enumeration value='VENDOR_SOFTWARE_INACTIVE'/>
          <xsd:enumeration value='USER_ALREADY_SUBSCRIBED'/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>


      <xsd:complexType name="CancelVendorAccessRequestReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
          <xsd:sequence>
            <xsd:element name="accessRequestToken" nillable="false" type="xsd:string"/>
            <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
          </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="CancelVendorAccessRequestResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
                <xsd:element name="errorCode" type="types:CancelVendorAccessRequestErrorEnum"/>
                <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="CancelVendorAccessRequestErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_VENDOR_SOFTWARE_ID"/>
          <xsd:enumeration value="INVALID_VENDOR_SESSION" />
          <xsd:enumeration value="OPERATOR_NOT_VENDORSOFTWARE_OWNER" />
          <xsd:enumeration value='INVALID_ACCESS_REQUEST_TOKEN'/>
          <xsd:enumeration value='INVALID_VENDOR_CLIENT_ACCESS_REQUEST_STATUS'/>
          <xsd:enumeration value='VENDOR_SOFTWARE_INVALID'/>
          <xsd:enumeration value='VENDOR_SOFTWARE_INACTIVE'/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="GetVendorAccessRequestsReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
          <xsd:sequence>
            <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
            <xsd:element name="status" type="types:VendorClientAccessRequestStatusEnum"/>
            <xsd:element name="requestDateFrom" nillable="true" type="xsd:dateTime"/>
            <xsd:element name="requestDateTo" nillable="true" type="xsd:dateTime"/>
          </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetVendorAccessRequestsResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
                <xsd:element name="vendorAccessRequests" nillable="true" type="types:ArrayOfVendorAccessRequest"/>
                <xsd:element name="errorCode" type="types:GetVendorAccessRequestsErrorEnum"/>
                <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfVendorAccessRequest">
        <xsd:sequence>
          <xsd:element name="vendorAccessRequest" form="qualified" maxOccurs="unbounded"
            nillable="true" type="types:VendorAccessRequest"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="VendorAccessRequest">
        <xsd:sequence>
        <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
        <xsd:element name="vendorCustomField" nillable="false" type="xsd:string"/>
        <xsd:element name="vendorClientId" nillable="false" type="xsd:int"/>
        <xsd:element name="accessRequestToken" nillable="false" type="xsd:string"/>
        <xsd:element name="expiryDate" nillable="false" type="xsd:dateTime"/>
        <xsd:element name="status" nillable="true" type="types:VendorClientAccessRequestStatusEnum"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="GetVendorAccessRequestsErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_VENDOR_SOFTWARE_ID"/>
          <xsd:enumeration value="INVALID_VENDOR_SESSION" />
          <xsd:enumeration value="OPERATOR_NOT_VENDORSOFTWARE_OWNER" />
          <xsd:enumeration value='VENDOR_SOFTWARE_INACTIVE'/>
          <xsd:enumeration value='INVALID_STATUS'/>
          <xsd:enumeration value='NO_RESULTS'/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:simpleType name="VendorClientAccessRequestStatusEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="ACTIVE"/>
          <xsd:enumeration value="CANCELLED"/>
          <xsd:enumeration value="EXPIRED"/>
          <xsd:enumeration value="DONE"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="CreateVendorAccessRequestReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
          <xsd:sequence>
            <xsd:element name="vendorCustomField" nillable="false" type="xsd:string"/>
            <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
            <xsd:element name="expiryDate" nillable="true" type="xsd:dateTime"/>
          </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="CreateVendorAccessRequestResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
                <xsd:element name="errorCode" type="types:CreateVendorAccessRequestErrorEnum"/>
                <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
                <xsd:element name="accessRequestToken" nillable="true" type="xsd:string"/>
                <xsd:element name="validUntil" type="xsd:dateTime"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="CreateVendorAccessRequestErrorEnum">
        <xsd:restriction base="xsd:string">
	        <xsd:enumeration value='OK'/>
	        <xsd:enumeration value='INVALID_VENDOR_SOFTWARE_ID'/>
	        <xsd:enumeration value='INVALID_VENDOR_SESSION'/>
	        <xsd:enumeration value='OPERATOR_NOT_VENDORSOFTWARE_OWNER'/>
	        <xsd:enumeration value='LOGIN_RESTRICTED_LOCATION'/>
	        <xsd:enumeration value='VENDOR_SOFTWARE_INVALID'/>
	        <xsd:enumeration value='VENDOR_SOFTWARE_INACTIVE'/>
	        <xsd:enumeration value='INVALID_VENDOR_CUSTOM_FIELD'/>
	        <xsd:enumeration value='INVALID_EXPIRY_DATE'/>
	        <xsd:enumeration value='API_ERROR'/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="VendorSubscriptionReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
	        <xsd:sequence>
		        <xsd:element name="username" nillable="false" type="xsd:string"/>
		        <xsd:element name="vendorCustomField" nillable="false" type="xsd:string"/>
		        <xsd:element name="vendorClientId" nillable="false" type="xsd:int"/>
		        <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
		        <xsd:element name="expiryDate" nillable="true" type="xsd:dateTime"/>
	        </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="VendorSubscriptionResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              	<xsd:element name="errorCode" type="types:VendorSubscriptionErrorEnum"/>
              	<xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              	<xsd:element name="validUntil" type="xsd:dateTime"/>
              	<xsd:element name="vendorClientId" nillable="false" type="xsd:int"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="VendorSubscriptionErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INVALID_USERNAME"/>
          <xsd:enumeration value="USER_NOT_ACCOUNT_OWNER"/>
          <xsd:enumeration value="INVALID_VENDOR_SOFTWARE_ID"/>
          <xsd:enumeration value="LOGIN_FAILED_ACCOUNT_LOCKED"/>
          <xsd:enumeration value="ACCOUNT_SUSPENDED"/>
          <xsd:enumeration value="ACCOUNT_CLOSED"/>
          <xsd:enumeration value="INVALID_VENDOR_SESSION" />
          <xsd:enumeration value="OPERATOR_NOT_VENDORSOFTWARE_OWNER" />
          <xsd:enumeration value="LOGIN_RESTRICTED_LOCATION"/>
          <xsd:enumeration value="USER_ALREADY_SUBSCRIBED"/>
          <xsd:enumeration value="INVALID_VENDOR_CLIENT_ID"/>
          <xsd:enumeration value="INVALID_VENDOR_CUSTOM_FIELD"/>
          <xsd:enumeration value="INVALID_INPUT_PARAMETERS"/>
          <xsd:enumeration value="API_ERROR"/>
        </xsd:restriction>
      </xsd:simpleType>
	  
      <xsd:complexType name="CancelVendorSubscriptionReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
	        <xsd:sequence>
		      <xsd:element name="username" nillable="false" type="xsd:string"/>
	          <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
	          <xsd:element name="vendorClientId" nillable="false" type="xsd:int"/>
			</xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="CancelVendorSubscriptionResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              	<xsd:element name="errorCode" type="types:VendorSubscriptionErrorEnum"/>
              	<xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
	  
      <xsd:complexType name="GetSubscriptionInfoReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
	        <xsd:sequence>
		      <xsd:element name="username" nillable="false" type="xsd:string"/>
		      <xsd:element name="vendorClientId" nillable="false" type="xsd:int"/>
		      <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
			</xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetSubscriptionInfoResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              	<xsd:element name="vendorSoftware" nillable="true" type="xsd:int"/>
              	<xsd:element name="expiryDate" nillable="true" type="xsd:dateTime"/>
              	<xsd:element name="errorCode" type="types:VendorSubscriptionErrorEnum"/>
              	<xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              	<xsd:element name="status" nillable="true" type="types:VendorSoftwareClientStatusEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
	  
      <xsd:complexType name="GetVendorInfoReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest"/>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="GetVendorInfoResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
				<xsd:element name="vendorInfo" nillable="true" type="types:ArrayOfVendorSoftwareInfos"/>
              	<xsd:element name="errorCode" type="types:VendorSubscriptionErrorEnum"/>
              	<xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfVendorSoftwareInfos">
        <xsd:sequence>
          <xsd:element name="vsInfo" form="qualified" maxOccurs="unbounded"
            nillable="true" type="types:VendorSoftwareInfo"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="VendorSoftwareInfo">
        <xsd:sequence>
          <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
          <xsd:element name="vendorSoftwareName" nillable="false" type="xsd:string"/>
          <xsd:element name="activeClientsNo" type="xsd:long"/>
        </xsd:sequence>
      </xsd:complexType>

      <xsd:complexType name="GetVendorUsersReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
	        <xsd:sequence>
	          <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
	          <xsd:element name="username" nillable="true" type="xsd:string"/>
	          <xsd:element name="usernameSearchModifier" type="types:SearchModifierEnum"/>
	          <xsd:element name="vendorCustomField" nillable="true" type="xsd:string"/>
	          <xsd:element name="customFieldSearchModifier" type="types:SearchModifierEnum"/>
	          <xsd:element name="expiryDateFrom" nillable="true" type="xsd:dateTime"/>
	          <xsd:element name="expiryDateTo" nillable="true" type="xsd:dateTime"/>
	          <xsd:element name="status" type="types:VendorSoftwareClientStatusEnum"/>
			</xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="SearchModifierEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="STARTS_WITH"/>
          <xsd:enumeration value="EXACT"/>
          <xsd:enumeration value="ENDS_WITH"/>
          <xsd:enumeration value="CONTAINS"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="GetVendorUsersResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
				<xsd:element name="vendorUsers" nillable="true" type="types:ArrayOfVendorUser"/>
              	<xsd:element name="errorCode" type="types:VendorSubscriptionErrorEnum"/>
              	<xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="ArrayOfVendorUser">
        <xsd:sequence>
          <xsd:element name="vendorUser" form="qualified" maxOccurs="unbounded"
            nillable="true" type="types:VendorUser"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="VendorUser">
        <xsd:sequence>
	      <xsd:element name="vendorSoftwareId" nillable="false" type="xsd:int"/>
	      <xsd:element name="username" nillable="false" type="xsd:string"/>
	      <xsd:element name="expiryDate" nillable="true" type="xsd:dateTime"/>
	      <xsd:element name="status" nillable="true" type="types:VendorSoftwareClientStatusEnum"/>
	      <xsd:element name="vendorClientId" nillable="false" type="xsd:int"/>
	      <xsd:element name="vendorCustomField" nillable="false" type="xsd:string"/>
	      <xsd:element name="createDate" nillable="true" type="xsd:dateTime"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="VendorSoftwareClientStatusEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="ACTIVE"/>
          <xsd:enumeration value="CANCELLED"/>
          <xsd:enumeration value="EXPIRED"/>
        </xsd:restriction>
      </xsd:simpleType>
	  
	  
	  <!-- base types copied from BFService wsdl-->
      <xsd:complexType abstract="true" name="APIRequest">
        <xsd:sequence>
          <xsd:element name="header" nillable="true" type="types:APIRequestHeader"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="APIRequestHeader">
        <xsd:sequence>
          <xsd:element name="clientStamp" type="xsd:long"/>
          <xsd:element name="sessionToken" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType abstract="true" name="APIResponse">
        <xsd:sequence>
          <xsd:element name="header" nillable="true" type="types:APIResponseHeader"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="APIResponseHeader">
        <xsd:sequence>
          <xsd:element name="errorCode" type="types:APIErrorEnum"/>
          <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
          <xsd:element name="sessionToken" nillable="true" type="xsd:string"/>
          <xsd:element name="timestamp" type="xsd:dateTime"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:simpleType name="APIErrorEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="OK"/>
          <xsd:enumeration value="INTERNAL_ERROR"/>
          <xsd:enumeration value="EXCEEDED_THROTTLE"/>
          <xsd:enumeration value="USER_NOT_SUBSCRIBED_TO_PRODUCT"/>
          <xsd:enumeration value="SUBSCRIPTION_INACTIVE_OR_SUSPENDED"/>
          <xsd:enumeration value="VENDOR_SOFTWARE_INACTIVE"/>
          <xsd:enumeration value="VENDOR_SOFTWARE_INVALID"/>
          <xsd:enumeration value="SERVICE_NOT_AVAILABLE_IN_PRODUCT"/>
          <xsd:enumeration value="NO_SESSION"/>
          <xsd:enumeration value="TOO_MANY_REQUESTS"/>
          <xsd:enumeration value="PRODUCT_REQUIRES_FUNDED_ACCOUNT"/>
          <xsd:enumeration value="SERVICE_NOT_AVAILABLE_FOR_LOGIN_STATUS"/>
        </xsd:restriction>
      </xsd:simpleType>
	  
    </xsd:schema>
    
    <xsd:schema elementFormDefault="qualified" targetNamespace="http://www.betfair.com/adminapi/v2/VendorService/">
      <xsd:import namespace="http://www.betfair.com/adminapi/types/v2/"/>

      <xsd:element name="setAccessRequest">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:SetAccessRequestReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="setAccessRequestResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:SetAccessRequestResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="cancelVendorAccessRequest">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:CancelVendorAccessRequestReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="cancelVendorAccessRequestResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:CancelVendorAccessRequestResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getVendorAccessRequests">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetVendorAccessRequestsReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getVendorAccessRequestsResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetVendorAccessRequestsResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="createVendorAccessRequest">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:CreateVendorAccessRequestReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="createVendorAccessRequestResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:CreateVendorAccessRequestResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="addVendorSubscription">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:VendorSubscriptionReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="addVendorSubscriptionResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:VendorSubscriptionResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="updateVendorSubscription">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:VendorSubscriptionReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="updateVendorSubscriptionResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:VendorSubscriptionResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="cancelVendorSubscription">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:CancelVendorSubscriptionReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="cancelVendorSubscriptionResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:CancelVendorSubscriptionResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getSubscriptionInfo">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetSubscriptionInfoReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getSubscriptionInfoResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetSubscriptionInfoResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getVendorInfo">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetVendorInfoReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getVendorInfoResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetVendorInfoResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="getVendorUsers">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:GetVendorUsersReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="getVendorUsersResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:GetVendorUsersResp"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

    </xsd:schema>

  </wsdl:types>

  <wsdl:message name="setAccessRequestIn">
    <wsdl:part element="tns:setAccessRequest" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="setAccessRequestOut">
    <wsdl:part element="tns:setAccessRequestResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="cancelVendorAccessRequestIn">
    <wsdl:part element="tns:cancelVendorAccessRequest" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="cancelVendorAccessRequestOut">
    <wsdl:part element="tns:cancelVendorAccessRequestResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getVendorAccessRequestsIn">
    <wsdl:part element="tns:getVendorAccessRequests" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getVendorAccessRequestsOut">
    <wsdl:part element="tns:getVendorAccessRequestsResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="createVendorAccessRequestIn">
    <wsdl:part element="tns:createVendorAccessRequest" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="createVendorAccessRequestOut">
    <wsdl:part element="tns:createVendorAccessRequestResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="addVendorSubscriptionIn">
    <wsdl:part element="tns:addVendorSubscription" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="addVendorSubscriptionOut">
    <wsdl:part element="tns:addVendorSubscriptionResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="updateVendorSubscriptionIn">
    <wsdl:part element="tns:updateVendorSubscription" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="updateVendorSubscriptionOut">
    <wsdl:part element="tns:updateVendorSubscriptionResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="cancelVendorSubscriptionIn">
    <wsdl:part element="tns:cancelVendorSubscription" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="cancelVendorSubscriptionOut">
    <wsdl:part element="tns:cancelVendorSubscriptionResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getSubscriptionInfoIn">
    <wsdl:part element="tns:getSubscriptionInfo" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getSubscriptionInfoOut">
    <wsdl:part element="tns:getSubscriptionInfoResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getVendorInfoIn">
    <wsdl:part element="tns:getVendorInfo" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getVendorInfoOut">
    <wsdl:part element="tns:getVendorInfoResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:message name="getVendorUsersIn">
    <wsdl:part element="tns:getVendorUsers" name="parameters"/>
  </wsdl:message>
  <wsdl:message name="getVendorUsersOut">
    <wsdl:part element="tns:getVendorUsersResponse" name="parameters"/>
  </wsdl:message>

  <wsdl:portType name="VendorService">

    <wsdl:operation name="setAccessRequest">
      <wsdl:input message="tns:setAccessRequestIn" name="setAccessRequestIn"/>
      <wsdl:output message="tns:setAccessRequestOut" name="setAccessRequestOut"/>
    </wsdl:operation>

    <wsdl:operation name="cancelVendorAccessRequest">
      <wsdl:input message="tns:cancelVendorAccessRequestIn" name="cancelVendorAccessRequestIn"/>
      <wsdl:output message="tns:cancelVendorAccessRequestOut" name="cancelVendorAccessRequestOut"/>
    </wsdl:operation>

    <wsdl:operation name="getVendorAccessRequests">
      <wsdl:input message="tns:getVendorAccessRequestsIn" name="getVendorAccessRequestsIn"/>
      <wsdl:output message="tns:getVendorAccessRequestsOut" name="getVendorAccessRequestsOut"/>
    </wsdl:operation>

    <wsdl:operation name="createVendorAccessRequest">
      <wsdl:input message="tns:createVendorAccessRequestIn" name="createVendorAccessRequestIn"/>
      <wsdl:output message="tns:createVendorAccessRequestOut" name="createVendorAccessRequestOut"/>
    </wsdl:operation>

    <wsdl:operation name="addVendorSubscription">
      <wsdl:input message="tns:addVendorSubscriptionIn" name="addVendorSubscriptionIn"/>
      <wsdl:output message="tns:addVendorSubscriptionOut" name="addVendorSubscriptionOut"/>
    </wsdl:operation>

    <wsdl:operation name="updateVendorSubscription">
      <wsdl:input message="tns:updateVendorSubscriptionIn" name="updateVendorSubscriptionIn"/>
      <wsdl:output message="tns:updateVendorSubscriptionOut" name="updateVendorSubscriptionOut"/>
    </wsdl:operation>

    <wsdl:operation name="cancelVendorSubscription">
      <wsdl:input message="tns:cancelVendorSubscriptionIn" name="cancelVendorSubscriptionIn"/>
      <wsdl:output message="tns:cancelVendorSubscriptionOut" name="cancelVendorSubscriptionOut"/>
    </wsdl:operation>

    <wsdl:operation name="getSubscriptionInfo">
      <wsdl:input message="tns:getSubscriptionInfoIn" name="getSubscriptionInfoIn"/>
      <wsdl:output message="tns:getSubscriptionInfoOut" name="getSubscriptionInfoOut"/>
    </wsdl:operation>

    <wsdl:operation name="getVendorInfo">
      <wsdl:input message="tns:getVendorInfoIn" name="getVendorInfoIn"/>
      <wsdl:output message="tns:getVendorInfoOut" name="getVendorInfoOut"/>
    </wsdl:operation>

    <wsdl:operation name="getVendorUsers">
      <wsdl:input message="tns:getVendorUsersIn" name="getVendorUsersIn"/>
      <wsdl:output message="tns:getVendorUsersOut" name="getVendorUsersOut"/>
    </wsdl:operation>

  </wsdl:portType>


  <wsdl:binding name="VendorService" type="tns:VendorService">
    <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>

    <wsdl:operation name="setAccessRequest">
      <soap:operation soapAction="setAccessRequest" style="document"/>
      <wsdl:input name="setAccessRequestIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="setAccessRequestOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="cancelVendorAccessRequest">
      <soap:operation soapAction="cancelVendorAccessRequest" style="document"/>
      <wsdl:input name="cancelVendorAccessRequestIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="cancelVendorAccessRequestOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="getVendorAccessRequests">
      <soap:operation soapAction="getVendorAccessRequests" style="document"/>
      <wsdl:input name="getVendorAccessRequestsIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getVendorAccessRequestsOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="createVendorAccessRequest">
      <soap:operation soapAction="createVendorAccessRequest" style="document"/>
      <wsdl:input name="createVendorAccessRequestIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="createVendorAccessRequestOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="addVendorSubscription">
      <soap:operation soapAction="addVendorSubscription" style="document"/>
      <wsdl:input name="addVendorSubscriptionIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="addVendorSubscriptionOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="updateVendorSubscription">
      <soap:operation soapAction="updateVendorSubscription" style="document"/>
      <wsdl:input name="updateVendorSubscriptionIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="updateVendorSubscriptionOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="cancelVendorSubscription">
      <soap:operation soapAction="cancelVendorSubscription" style="document"/>
      <wsdl:input name="cancelVendorSubscriptionIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="cancelVendorSubscriptionOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="getSubscriptionInfo">
      <soap:operation soapAction="getSubscriptionInfo" style="document"/>
      <wsdl:input name="getSubscriptionInfoIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getSubscriptionInfoOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="getVendorInfo">
      <soap:operation soapAction="getVendorInfo" style="document"/>
      <wsdl:input name="getVendorInfoIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getVendorInfoOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

    <wsdl:operation name="getVendorUsers">
      <soap:operation soapAction="getVendorUsers" style="document"/>
      <wsdl:input name="getVendorUsersIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="getVendorUsersOut">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>

  </wsdl:binding>
  <wsdl:service name="VendorService">
    <wsdl:port binding="tns:VendorService" name="VendorService">
      <soap:address location="https://api.betfair.com/admin-api/v2/VendorService"/>
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>
'''
