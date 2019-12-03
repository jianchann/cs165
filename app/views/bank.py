from app import app, db, redis_store, utils
from app.models import Bank, Branch, BankAccount, Tin, CountryofResidence, CountryinAddress, PostalCode, Account, Form

import requests
import datetime
from flask import Flask, jsonify, g, render_template, redirect, request

@app.route('/bank', methods=['GET'])
def get_banks():
    banks = Bank.query.all()
    if len(banks) == 0:
        bankNames = ["Metrobank","Unionbank of the Philippines","Land Bank of the Philippines","Banco de Oro","Bank of the Philippine Islands"]
        bankAddresses = ["Metrobank Plaza, Sen. Gil J. Puyat Avenue, Makati City","UnionBank Plaza Bldg., Meralco Avenue, Pasig City","LANDBANK Plaza, 1598 M.H. del Pilar, Manila City","7899 Makati Avenue, Makati City","6768 Ayala Avenue, Makati City"]
        for i in range(0,len(bankNames)):
            bank = Bank(
                bankName=bankNames[i],
                bankMainAddress=bankAddresses[i]
            )
            db.session.add(bank)
        db.session.commit()
        return get_banks()
    else:
        return_data = []
        for bank in banks:
            branch_list = []
            bankaccount_list = []
            branches = bank.bankBranches
            for branch in branches:
                branch_list.append(branch.bankBranchName)
            bankaccounts = bank.bankAccounts
            for bankaccount in bankaccounts:
                bankaccount_list.append(str(bankaccount.bankAcctNo))
            return_data.append({
                "bankName": bank.bankName,
                "bankMainAddress": bank.bankMainAddress,
                "bankBranches": branch_list,
                "bankAccounts": bankaccount_list,
            })
        return jsonify(return_data)


@app.route('/bank/create', methods=['POST'])
def create_bank():
    post_data = request.get_json()
    bankName = post_data.get('bankName')
    bankMainAddress = post_data.get('bankMainAddress')

    bank = Bank(
        bankName=bankName,
        bankMainAddress=bankMainAddress
    )

    db.session.add(bank)

    db.session.commit()

    return jsonify({'msg': "SUCCESS"})