import time

# Baseline registry values (simulated)
baseline = {
    "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run": "safe.exe"
}

print("Baseline Registry Snapshot Created")

while True:
    # Simulated current registry values (change this to test)
    current = {
        "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run": "malware.exe"
    }

    print("\nMonitoring registry...")

    for key in current:
        if baseline.get(key) != current[key]:
            print("⚠️ ALERT: Registry change detected!")
            print("Key:", key)
            print("Old Value:", baseline.get(key))
            print("New Value:", current[key])

            # Log file me save karo
            with open("registry_log.txt", "a") as log:
                log.write(f"Change detected in {key}\n")
                log.write(f"Old: {baseline.get(key)} | New: {current[key]}\n\n")

    time.sleep(5)  # 5 sec baad check
