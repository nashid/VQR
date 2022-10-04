import torch
import torch.nn as nn


class CrossT5(nn.Module):
    def __init__(self, t5, tokenizer, args):
        super(CrossT5, self).__init__()
        self.t5 = t5
        self.tokenizer = tokenizer
        self.args = args

    def forward(self,
                input_ids,
                vul_query_label=None,
                repair_input_ids=None,
                generate_repair=False):
        # prepare all attention masks
        attention_mask = input_ids.ne(self.tokenizer.pad_token_id)
        if generate_repair:
            beam_outputs = self.t5.generate(input_ids=input_ids,
                                          attention_mask=attention_mask,
                                          do_sample=False, # disable sampling to test if batching affects output
                                          num_beams=self.args.num_beams,
                                          num_return_sequences=self.args.num_beams,
                                          max_length=self.args.vul_repair_block_size,
                                          vul_query=vul_query_label)
            return beam_outputs
        else:
            loss = self.t5(input_ids=input_ids, attention_mask=attention_mask, vul_query=vul_query_label, labels=repair_input_ids).loss
            return loss
