# Beacons Project

## AP BLE Detection

### `Data Structure`

**`By venue`**

- `API Url`: */stream/:venueId/presence* --- for data from all Gateways assigned to a single Location (Venue)
- `venueId`: *19635d7f-76fc-4347-8e00-a4163f7fe180*
- `Data`:

		deviceAddress: null // if beacon, it returns mac-address
		proximity: "FAR" // ("IMMEDIATE", "NEAR", "FAR")
		rssi: -95
		scanType: "BLE" // signal
		sourceId: "0C:8D:DB:D9:0D:5B" // AP address
		timestamp: 1550526269
		trackingId: "7C:04:D0:C4:AE:D1" // if beacon, it return beaconid, else device mac-address (smartphone)

**`By AP`**

- `API Url`: */presence/stream/:receiverId* --- for data from a single Gateway
- `receiverId`: *0C:8D:DB:D9:0D:5B* - AP
- `Data`:

		deviceAddress: null // if beacon, it returns mac-address
		proximity: "NEAR" // ("IMMEDIATE", "NEAR", "FAR")
		rssi: -86
		scanType: "BLE" // signal
		sourceId: "0C:8D:DB:D9:0D:5B" // AP address
		timestamp: 1550526971
		trackingId: "5C:49:7D:AB:6E:19" // if beacon, it return beaconid, else device mac-address (smartphone)

