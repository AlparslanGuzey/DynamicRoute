def extract_payload_epsilon_data(segment_details):
    payloads = []
    epsilons = []
    for segment in segment_details:
        if isinstance(segment, dict):
            payloads.append(segment.get('payload', 0))
            epsilons.append(segment.get('epsilon', 0))
        else:
            print("Error: segment is not a dictionary. Check the structure of segment_details.")
    return payloads, epsilons