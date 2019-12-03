from app import app, db, redis_store, utils
from app.models import Bank, Branch, BankAccount, Tin, CountryofResidence, CountryinAddress, PostalCode, Account, Form

import requests
import datetime
from flask import Flask, jsonify, g, render_template, redirect, request

@app.route('/bankaccount', methods=['GET'])
def get_bankaccts():
    # SELECT:
    # SELECT * FROM BankAccount NATURAL JOIN Bank NATURAL Branch;
    bankaccts = BankAccount.query.all()
    if len(bankaccts) == 0:
        # POPULATE
        # INSERT INTO BankAccount VALUES
        # (123756789122421,"Bank of the Philippine Islands", "BPI UP Town Center"),
        # (341256989113453,"Bank of the Philippine Islands", "BPI Loyola-Katipunan"),
        # (563412089153456,"Banco de Oro", "BDO Katipunan"),
        # (783456389121450,"Metrobank", "Metrobank Katipunan"),
        # (903456189125451,"Metrobank", "Metrobank Blue Ridge");
        acctNos = [123756789122421,341256989113453,563412089153456,783456389121450,903456189125451]
        bankNames = [
            "Bank of the Philippine Islands",
            "Bank of the Philippine Islands",
            "Banco de Oro",
            "Metrobank",
            "Metrobank"
        ]
        branchNames = [
            "BPI UP Town Center",
            "BPI Loyola-Katipunan",
            "BDO Katipunan",
            "Metrobank Katipunan",
            "Metrobank Blue Ridge"
        ]
        for i in range(0, len(acctNos)):
            bankacct = BankAccount(
                bankAcctNo=acctNos[i],
                bankName=bankNames[i],
                bankBranchName=branchNames[i]
            )
            db.session.add(bankacct)
        db.session.commit()
        return get_bankaccts()
    else:    
        return_data = []
        for bankacct in bankaccts:
            return_data.append({
                "bankAcctNo": str(bankacct.bankAcctNo),
                "bankName": bankacct.bankName,
                "bankMainAddress": bankacct.bank.bankMainAddress,
                "bankBranchName": bankacct.bankBranchName,
                "bankBranchAddress": bankacct.branch.bankBranchAddress
            })
        return jsonify(return_data)


@app.route('/bankaccount/create', methods=['POST'])
def create_bankacct():
    # INSERT:
    # INSERT INTO BankAccount VALUES (<BankAcctNo>, <bankName>, <bankBranchName>);
    post_data = request.get_json()
    bankAcctNo = post_data.get('bankAcctNo')
    bankName = post_data.get('bankName')
    bankBranchName = post_data.get('bankBranchName')
    bank = Bank.query.get(bankName)
    branch = Branch.query.get(bankBranchName)

    bankacct = BankAccount(
        bankAcctNo=bankAcctNo,
        bankName=bankName,
        bankBranchName=bankBranchName
    )
    db.session.add(bankacct)
    bank.bankAccounts.append(bankacct)
    branch.bankAccounts.append(bankacct)

    db.session.commit()

    return jsonify({'msg': "SUCCESS"})

@app.route('/bankaccount/update', methods=['PUT'])
def update_bankacct():
    # UPDATE:
    # UPDATE BankAccount SET bankAcctNo = <bankAcctNo>, bankName = <bankName>, bankBranchName = <bankBranchName>
    # WHERE bankAcctNo = <currentBankAcctNo> AND bankName = <currentBankName>
    post_data = request.get_json()
    currentBankAcctNo = post_data.get('currentBankAcctNo')
    currentBankName = post_data.get('currentBankName')
    bankacct = BankAccount.query.get((currentBankAcctNo,currentBankName))
    bankAcctNo = post_data.get('bankAcctNo')
    bankName = post_data.get('bankName')
    bankBranchName = post_data.get('bankBranchName')

    if currentBankName != bankName:
        newBank = Bank.query.get(bankName)
        newBank.bankAccounts.append(bankacct)

    if bankacct.bankBranchName != bankBranchName:
        newBranch = Branch.query.get(bankBranchName)
        newBranch.bankAccounts.append(bankacct)

    bankacct.bankAcctNo = bankAcctNo
    db.session.commit()

    return jsonify({'msg': "SUCCESS"})

@app.route('/bankaccount/delete', methods=['POST'])
def delete_bankacct():
    # DELETE:
    # DELETE FROM BankAccount WHERE bankAcctNo = <bankAcctNo> AND bankName = <bankName>;
    post_data = request.get_json()
    bankAcctNo = post_data.get('bankAcctNo')
    bankName = post_data.get('bankName')
    bankacct = BankAccount.query.get((bankAcctNo,bankName))
    db.session.delete(bankacct)
    db.session.commit()

    return jsonify({'msg': "SUCCESS"})