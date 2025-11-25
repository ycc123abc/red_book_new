        # S = "abcdef0123456789"
        # k=16
        # function generateTraceId() {
        #     for (var e = "", a = 0; a < 16; a++)
        #         e += S.charAt(Math.floor(Math.random() * k));
        #     return e
        # }
import random

class  B3TraceIdGenerator:
    def get_b3_trace_id():
        S = "abcdef0123456789"
        k = 16
        trace_id = ""
        for _ in range(k):
            trace_id += random.choice(S)
        return trace_id




