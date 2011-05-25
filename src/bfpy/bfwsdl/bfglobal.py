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
			<!-- The following four values added for new withdrawByBankTransfer operation -->
			<!-- Do not use unless for other operations unless they are also new.  There  -->
			<!-- will be some clients that are not aware of these new enum values.        -->			        
            <xsd:enumeration value="DEPOSITS_NOT_CLEARED"/>
            <xsd:enumeration value="INVALID_BANK_ACCOUNT_DETAILS_FIELD"/>
            <xsd:enumeration value="EXPRESS_TRANSFER_NOT_AVAILABLE"/>
            <xsd:enumeration value="UNSUPPORTED_COUNTRY_FOR_BANK_TRANSFER"/>
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

      <xsd:complexType name="WithdrawByBankTransferReq">
        <xsd:complexContent>
          <xsd:extension base="types:APIRequest">
            <xsd:sequence>
              <xsd:element name="mode" nillable="false" type="types:WithdrawByBankTransferModeEnum"/>
              <xsd:element name="amount" nillable="false" type="xsd:double"/>
              <xsd:element name="bankAccountDetails" nillable="false"
                type="types:BankAccountDetails"/>
              <xsd:element name="expressTransfer" nillable="false" type="xsd:boolean"/>
              <xsd:element name="password" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:complexType name="WithdrawByBankTransferResp">
        <xsd:complexContent>
          <xsd:extension base="types:APIResponse">
            <xsd:sequence>
              <xsd:element name="errorCode" nillable="false" type="types:PaymentsErrorEnum"/>
              <xsd:element name="minorErrorCode" nillable="true" type="xsd:string"/>
              <xsd:element name="amountWithdrawn" nillable="false" type="xsd:double"/>
              <xsd:element name="minAmount" nillable="false" type="xsd:double"/>
              <xsd:element name="maxAmount" nillable="false" type="xsd:double"/>
              <xsd:element name="amountAvailable" nillable="true" type="xsd:double"/>
              <xsd:element name="transferFee" nillable="true" type="xsd:double"/>
              <xsd:element name="expressTransferFee" nillable="true" type="xsd:double"/>
              <xsd:element name="expressTransferAvailable" nillable="true" type="xsd:boolean"/>
              <xsd:element name="lastBankAccountDetails" nillable="true"
                type="types:BankAccountDetails"/>
              <xsd:element name="requiredBankAccountDetailsFields" nillable="true"
                type="types:ArrayOfBankAccountDetailsField"/>
              <xsd:element name="transactionId" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="WithdrawByBankTransferModeEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="VALIDATE"/>
          <xsd:enumeration value="EXECUTE"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="ArrayOfBankAccountDetailsField">
        <xsd:sequence>
          <xsd:element form="qualified" maxOccurs="unbounded" name="BankAccountDetailsField"
            nillable="true" type="types:BankAccountDetailsField"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="BankAccountDetailsField">
        <xsd:complexContent>
          <xsd:extension base="types:AbstractField">
            <xsd:sequence>
              <xsd:element name="type" nillable="false" type="types:BankAccountDetailsFieldEnum"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="BankAccountDetailsFieldEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="PAYEE"/>
          <xsd:enumeration value="BANK_LOCATION_ISO3"/>
          <xsd:enumeration value="BANK_NAME"/>
          <xsd:enumeration value="ACCOUNT_HOLDING_BRANCH"/>
          <xsd:enumeration value="ACCOUNT_NUMBER"/>
          <xsd:enumeration value="ACCOUNT_TYPE"/>
          <xsd:enumeration value="BANK_CODE"/>
          <xsd:enumeration value="SORT_CODE"/>
          <xsd:enumeration value="BANK_KEY"/>
          <xsd:enumeration value="BRANCH_CODE"/>
          <xsd:enumeration value="ROUTING"/>
          <xsd:enumeration value="BANK_BSB"/>
          <xsd:enumeration value="BLZ_CODE"/>
          <xsd:enumeration value="ABI_CAB"/>
          <xsd:enumeration value="BANK_GIRO_CREDIT_NUMBER"/>
        </xsd:restriction>
      </xsd:simpleType>
      <xsd:complexType name="AbstractField">
        <xsd:sequence>
          <xsd:element name="required" nillable="false" type="xsd:boolean"/>
          <xsd:element name="readOnly" nillable="false" type="xsd:boolean"/>
          <xsd:element name="size" nillable="false" type="xsd:int"/>
          <xsd:element name="minLength" nillable="false" type="xsd:int"/>
          <xsd:element name="maxLength" nillable="false" type="xsd:int"/>
          <xsd:element name="regExp" nillable="false" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="BasicBankAccountDetails">
        <xsd:sequence>
          <xsd:element name="bankName" nillable="true" type="xsd:string"/>
          <xsd:element name="accountHoldingBranch" nillable="true" type="xsd:string"/>
          <xsd:element name="bankGiroCreditNumber" nillable="true" type="xsd:string"/>
          <xsd:element name="accountNumber" nillable="true" type="xsd:string"/>
          <xsd:element name="sortCode" nillable="true" type="xsd:string"/>
          <xsd:element name="bankCode" nillable="true" type="xsd:string"/>
          <xsd:element name="blzCode" nillable="true" type="xsd:string"/>
          <xsd:element name="bankBsb" nillable="true" type="xsd:string"/>
          <xsd:element name="branchCode" nillable="true" type="xsd:string"/>
          <xsd:element name="bankLocationIso3" nillable="true" type="xsd:string"/>
        </xsd:sequence>
      </xsd:complexType>
      <xsd:complexType name="BankAccountDetails">
        <xsd:complexContent>
          <xsd:extension base="types:BasicBankAccountDetails">
            <xsd:sequence>
              <xsd:element name="payee" nillable="true" type="xsd:string"/>
              <xsd:element name="accountType" nillable="false" type="types:BankAccountTypeEnum"/>
              <xsd:element name="bankKey" nillable="true" type="xsd:string"/>
              <xsd:element name="routing" nillable="true" type="xsd:string"/>
              <xsd:element name="abiCab" nillable="true" type="xsd:string"/>
            </xsd:sequence>
          </xsd:extension>
        </xsd:complexContent>
      </xsd:complexType>
      <xsd:simpleType name="BankAccountTypeEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="NotSpecified"/>
          <xsd:enumeration value="CH"/>
          <xsd:enumeration value="SA"/>
          <xsd:enumeration value="TR"/>
        </xsd:restriction>
      </xsd:simpleType>

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
      
      <xsd:simpleType name="ViewProfileV2ReqVersionEnum">
        <xsd:restriction base="xsd:string">
          <xsd:enumeration value="V1"/>
        </xsd:restriction>
      </xsd:simpleType>

      <xsd:complexType name="ViewProfileV2Req">
        <xsd:complexContent>
          <xsd:extension base='types:APIRequest'>
        	<xsd:sequence>
        		<xsd:element name='requestVersion' nillable='true' type='types:ViewProfileV2ReqVersionEnum'/>
        	</xsd:sequence>
        </xsd:extension>
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
              <xsd:element name='nationalIdentifier' minOccurs='0' type='xsd:string'/>
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
              <xsd:element name="depositLimitFrequency" nillable='true' type="types:GamcareLimitFreqEnum"/>
              <xsd:element name="lossLimit" nillable="true" type="xsd:int"/>
              <xsd:element name="lossLimitFrequency" nillable='true' type="types:GamcareLimitFreqEnum"/>
              <xsd:element name='nationalIdentifier' nillable='true' type='xsd:string'/>
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
              <xsd:element name="nationalIdentifier" nillable="true" type="xsd:string"/>                  
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

      <xsd:element name="withdrawByBankTransfer">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="request" type="types:WithdrawByBankTransferReq"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="withdrawByBankTransferResponse">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Result" nillable="true" type="types:WithdrawByBankTransferResp"/>
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
  <wsdl:message name="withdrawByBankTransferIn">
    <wsdl:part name="parameters" element="tns:withdrawByBankTransfer"/>
  </wsdl:message>
  <wsdl:message name="withdrawByBankTransferOut">
    <wsdl:part name="parameters" element="tns:withdrawByBankTransferResponse"/>
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
    <wsdl:operation name="withdrawByBankTransfer">
      <wsdl:input name="withdrawByBankTransferIn" message="tns:withdrawByBankTransferIn"/>
      <wsdl:output name="withdrawByBankTransferOut" message="tns:withdrawByBankTransferOut"/>
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
    <wsdl:operation name="withdrawByBankTransfer">
      <soap:operation soapAction="withdrawByBankTransfer" style="document"/>
      <wsdl:input name="withdrawByBankTransferIn">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="withdrawByBankTransferOut">
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
