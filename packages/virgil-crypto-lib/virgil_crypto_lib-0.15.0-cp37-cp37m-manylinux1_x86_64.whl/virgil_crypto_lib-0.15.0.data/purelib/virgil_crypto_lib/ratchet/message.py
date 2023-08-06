# Copyright (C) 2015-2020 Virgil Security, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     (1) Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#
#     (2) Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
#
#     (3) Neither the name of the copyright holder nor the names of its
#     contributors may be used to endorse or promote products derived from
#     this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ''AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Lead Maintainer: Virgil Security Inc. <support@virgilsecurity.com>


from ctypes import *
from ._c_bridge import VscrRatchetMessage
from virgil_crypto_lib.common._c_bridge import Data
from virgil_crypto_lib.common._c_bridge import Buffer
from ._c_bridge._vscr_error import vscr_error_t
from .message import Message
from ._c_bridge import VscrStatus


class Message(object):
    """Class represents ratchet message"""

    def __init__(self):
        """Create underlying C context."""
        self._lib_vscr_ratchet_message = VscrRatchetMessage()
        self.ctx = self._lib_vscr_ratchet_message.vscr_ratchet_message_new()

    def __delete__(self, instance):
        """Destroy underlying C context."""
        self._lib_vscr_ratchet_message.vscr_ratchet_message_delete(self.ctx)

    def get_type(self):
        """Returns message type."""
        result = self._lib_vscr_ratchet_message.vscr_ratchet_message_get_type(self.ctx)
        return result

    def get_counter(self):
        """Returns message counter in current asymmetric ratchet round."""
        result = self._lib_vscr_ratchet_message.vscr_ratchet_message_get_counter(self.ctx)
        return result

    def get_sender_identity_key_id(self):
        """Returns long-term public key, if message is prekey message."""
        result = self._lib_vscr_ratchet_message.vscr_ratchet_message_get_sender_identity_key_id(self.ctx)
        instance = Data.take_c_ctx(result)
        cleaned_bytes = bytearray(instance)
        return cleaned_bytes

    def get_receiver_identity_key_id(self):
        """Returns long-term public key, if message is prekey message."""
        result = self._lib_vscr_ratchet_message.vscr_ratchet_message_get_receiver_identity_key_id(self.ctx)
        instance = Data.take_c_ctx(result)
        cleaned_bytes = bytearray(instance)
        return cleaned_bytes

    def get_receiver_long_term_key_id(self):
        """Returns long-term public key, if message is prekey message."""
        result = self._lib_vscr_ratchet_message.vscr_ratchet_message_get_receiver_long_term_key_id(self.ctx)
        instance = Data.take_c_ctx(result)
        cleaned_bytes = bytearray(instance)
        return cleaned_bytes

    def get_receiver_one_time_key_id(self):
        """Returns one-time public key, if message is prekey message and if one-time key is present, empty result otherwise."""
        result = self._lib_vscr_ratchet_message.vscr_ratchet_message_get_receiver_one_time_key_id(self.ctx)
        instance = Data.take_c_ctx(result)
        cleaned_bytes = bytearray(instance)
        return cleaned_bytes

    def serialize_len(self):
        """Buffer len to serialize this class."""
        result = self._lib_vscr_ratchet_message.vscr_ratchet_message_serialize_len(self.ctx)
        return result

    def serialize(self):
        """Serializes instance."""
        output = Buffer(self.serialize_len())
        self._lib_vscr_ratchet_message.vscr_ratchet_message_serialize(self.ctx, output.c_buffer)
        return output.get_bytes()

    def deserialize(self, input):
        """Deserializes instance."""
        d_input = Data(input)
        error = vscr_error_t()
        result = self._lib_vscr_ratchet_message.vscr_ratchet_message_deserialize(d_input.data, error)
        VscrStatus.handle_status(error.status)
        instance = Message.take_c_ctx(result)
        return instance

    @classmethod
    def take_c_ctx(cls, c_ctx):
        inst = cls.__new__(cls)
        inst._lib_vscr_ratchet_message = VscrRatchetMessage()
        inst.ctx = c_ctx
        return inst

    @classmethod
    def use_c_ctx(cls, c_ctx):
        inst = cls.__new__(cls)
        inst._lib_vscr_ratchet_message = VscrRatchetMessage()
        inst.ctx = inst._lib_vscr_ratchet_message.vscr_ratchet_message_shallow_copy(c_ctx)
        return inst
