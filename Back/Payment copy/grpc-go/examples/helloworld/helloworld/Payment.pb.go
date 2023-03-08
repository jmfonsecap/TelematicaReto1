// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.1
// 	protoc        v4.22.0
// source: helloworld/Payment.proto

package helloworld

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type ItemId struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	PedidoId int32 `protobuf:"varint,1,opt,name=pedidoId,proto3" json:"pedidoId,omitempty"`
}

func (x *ItemId) Reset() {
	*x = ItemId{}
	if protoimpl.UnsafeEnabled {
		mi := &file_helloworld_Payment_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ItemId) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ItemId) ProtoMessage() {}

func (x *ItemId) ProtoReflect() protoreflect.Message {
	mi := &file_helloworld_Payment_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ItemId.ProtoReflect.Descriptor instead.
func (*ItemId) Descriptor() ([]byte, []int) {
	return file_helloworld_Payment_proto_rawDescGZIP(), []int{0}
}

func (x *ItemId) GetPedidoId() int32 {
	if x != nil {
		return x.PedidoId
	}
	return 0
}

type None struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *None) Reset() {
	*x = None{}
	if protoimpl.UnsafeEnabled {
		mi := &file_helloworld_Payment_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *None) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*None) ProtoMessage() {}

func (x *None) ProtoReflect() protoreflect.Message {
	mi := &file_helloworld_Payment_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use None.ProtoReflect.Descriptor instead.
func (*None) Descriptor() ([]byte, []int) {
	return file_helloworld_Payment_proto_rawDescGZIP(), []int{1}
}

type Respuesta struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	StatusCode int32  `protobuf:"varint,1,opt,name=status_code,json=statusCode,proto3" json:"status_code,omitempty"`
	Message    string `protobuf:"bytes,2,opt,name=message,proto3" json:"message,omitempty"`
}

func (x *Respuesta) Reset() {
	*x = Respuesta{}
	if protoimpl.UnsafeEnabled {
		mi := &file_helloworld_Payment_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Respuesta) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Respuesta) ProtoMessage() {}

func (x *Respuesta) ProtoReflect() protoreflect.Message {
	mi := &file_helloworld_Payment_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Respuesta.ProtoReflect.Descriptor instead.
func (*Respuesta) Descriptor() ([]byte, []int) {
	return file_helloworld_Payment_proto_rawDescGZIP(), []int{2}
}

func (x *Respuesta) GetStatusCode() int32 {
	if x != nil {
		return x.StatusCode
	}
	return 0
}

func (x *Respuesta) GetMessage() string {
	if x != nil {
		return x.Message
	}
	return ""
}

var File_helloworld_Payment_proto protoreflect.FileDescriptor

var file_helloworld_Payment_proto_rawDesc = []byte{
	0x0a, 0x18, 0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x77, 0x6f, 0x72, 0x6c, 0x64, 0x2f, 0x50, 0x61, 0x79,
	0x6d, 0x65, 0x6e, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x24, 0x0a, 0x06, 0x49, 0x74,
	0x65, 0x6d, 0x49, 0x64, 0x12, 0x1a, 0x0a, 0x08, 0x70, 0x65, 0x64, 0x69, 0x64, 0x6f, 0x49, 0x64,
	0x18, 0x01, 0x20, 0x01, 0x28, 0x05, 0x52, 0x08, 0x70, 0x65, 0x64, 0x69, 0x64, 0x6f, 0x49, 0x64,
	0x22, 0x06, 0x0a, 0x04, 0x4e, 0x6f, 0x6e, 0x65, 0x22, 0x46, 0x0a, 0x09, 0x52, 0x65, 0x73, 0x70,
	0x75, 0x65, 0x73, 0x74, 0x61, 0x12, 0x1f, 0x0a, 0x0b, 0x73, 0x74, 0x61, 0x74, 0x75, 0x73, 0x5f,
	0x63, 0x6f, 0x64, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0a, 0x73, 0x74, 0x61, 0x74,
	0x75, 0x73, 0x43, 0x6f, 0x64, 0x65, 0x12, 0x18, 0x0a, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67,
	0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x07, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65,
	0x32, 0x5d, 0x0a, 0x07, 0x50, 0x61, 0x79, 0x6d, 0x65, 0x6e, 0x74, 0x12, 0x25, 0x0a, 0x0e, 0x50,
	0x61, 0x67, 0x61, 0x72, 0x54, 0x6f, 0x64, 0x6f, 0x43, 0x61, 0x72, 0x72, 0x6f, 0x12, 0x05, 0x2e,
	0x4e, 0x6f, 0x6e, 0x65, 0x1a, 0x0a, 0x2e, 0x52, 0x65, 0x73, 0x70, 0x75, 0x65, 0x73, 0x74, 0x61,
	0x22, 0x00, 0x12, 0x2b, 0x0a, 0x12, 0x50, 0x61, 0x67, 0x61, 0x72, 0x49, 0x74, 0x65, 0x6d, 0x45,
	0x6e, 0x45, 0x6c, 0x43, 0x61, 0x72, 0x72, 0x6f, 0x12, 0x07, 0x2e, 0x49, 0x74, 0x65, 0x6d, 0x49,
	0x64, 0x1a, 0x0a, 0x2e, 0x52, 0x65, 0x73, 0x70, 0x75, 0x65, 0x73, 0x74, 0x61, 0x22, 0x00, 0x42,
	0x67, 0x0a, 0x1b, 0x69, 0x6f, 0x2e, 0x67, 0x72, 0x70, 0x63, 0x2e, 0x65, 0x78, 0x61, 0x6d, 0x70,
	0x6c, 0x65, 0x73, 0x2e, 0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x77, 0x6f, 0x72, 0x6c, 0x64, 0x42, 0x0f,
	0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x57, 0x6f, 0x72, 0x6c, 0x64, 0x50, 0x72, 0x6f, 0x74, 0x6f, 0x50,
	0x01, 0x5a, 0x35, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x67, 0x6f, 0x6c, 0x61, 0x6e, 0x67,
	0x2e, 0x6f, 0x72, 0x67, 0x2f, 0x67, 0x72, 0x70, 0x63, 0x2f, 0x65, 0x78, 0x61, 0x6d, 0x70, 0x6c,
	0x65, 0x73, 0x2f, 0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x77, 0x6f, 0x72, 0x6c, 0x64, 0x2f, 0x68, 0x65,
	0x6c, 0x6c, 0x6f, 0x77, 0x6f, 0x72, 0x6c, 0x64, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_helloworld_Payment_proto_rawDescOnce sync.Once
	file_helloworld_Payment_proto_rawDescData = file_helloworld_Payment_proto_rawDesc
)

func file_helloworld_Payment_proto_rawDescGZIP() []byte {
	file_helloworld_Payment_proto_rawDescOnce.Do(func() {
		file_helloworld_Payment_proto_rawDescData = protoimpl.X.CompressGZIP(file_helloworld_Payment_proto_rawDescData)
	})
	return file_helloworld_Payment_proto_rawDescData
}

var file_helloworld_Payment_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_helloworld_Payment_proto_goTypes = []interface{}{
	(*ItemId)(nil),    // 0: ItemId
	(*None)(nil),      // 1: None
	(*Respuesta)(nil), // 2: Respuesta
}
var file_helloworld_Payment_proto_depIdxs = []int32{
	1, // 0: Payment.PagarTodoCarro:input_type -> None
	0, // 1: Payment.PagarItemEnElCarro:input_type -> ItemId
	2, // 2: Payment.PagarTodoCarro:output_type -> Respuesta
	2, // 3: Payment.PagarItemEnElCarro:output_type -> Respuesta
	2, // [2:4] is the sub-list for method output_type
	0, // [0:2] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_helloworld_Payment_proto_init() }
func file_helloworld_Payment_proto_init() {
	if File_helloworld_Payment_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_helloworld_Payment_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ItemId); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_helloworld_Payment_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*None); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_helloworld_Payment_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Respuesta); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_helloworld_Payment_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_helloworld_Payment_proto_goTypes,
		DependencyIndexes: file_helloworld_Payment_proto_depIdxs,
		MessageInfos:      file_helloworld_Payment_proto_msgTypes,
	}.Build()
	File_helloworld_Payment_proto = out.File
	file_helloworld_Payment_proto_rawDesc = nil
	file_helloworld_Payment_proto_goTypes = nil
	file_helloworld_Payment_proto_depIdxs = nil
}
