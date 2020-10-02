import ibm_db

try:
    client = ibm_db.pconnect(
        "DATABASE=" + "BLUDB" +
        ";HOSTNAME=" + "zen-cpd-zen.cp4docp43cluster-8bd82ab93bc861f858890126d8105068-0000.us-east.containers.appdomain.cloud" +
        ";PORT=" + "30662" +
        ";UID=" + "user1011" +
        ";PWD=" + "b_mOC?5zM@5?1N8n",
        "", "")

    state = ibm_db.active(client)

# handle exceptions later TODO
except Exception as e:
    raise e

print(state)
