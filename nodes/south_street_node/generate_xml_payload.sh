#!/bin/bash
# XML Transmission Payload Generator

OUTPUT_FILE="$HOME/Jackson-Node/nodes/south_street_node/docs/transmission.xml"

# Constructing the XML Body
cat <<EOF > "$OUTPUT_FILE"
<PropertySubmission>
    <Header>
        <NodeID>South_Street_Node_01</NodeID>
        <Timestamp>$(date -u +"%Y-%m-%dT%H:%M:%SZ")</Timestamp>
    </Header>
    <Payload>
        <Address>1002 E South Street, Jackson, MI 49203</Address>
        <Action>PURCHASE_INTENT</Action>
        <Specs>
            <Size>17692</Size>
            <Units>sqft</Units>
            <Zoning>I-2</Zoning>
        </Specs>
    </Payload>
</PropertySubmission>
EOF

echo "XML Payload generated at $OUTPUT_FILE"

