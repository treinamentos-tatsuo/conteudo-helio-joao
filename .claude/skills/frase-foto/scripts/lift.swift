// Recorta a pessoa da foto (máscara Vision do macOS). uso: swift lift.swift entrada.png saida.png
import Vision
import CoreImage
import AppKit
let a = CommandLine.arguments
let handler = VNImageRequestHandler(url: URL(fileURLWithPath: a[1]))
let req = VNGenerateForegroundInstanceMaskRequest()
try handler.perform([req])
guard let r = req.results?.first else { print("sem pessoa"); exit(1) }
let buf = try r.generateMaskedImage(ofInstances: r.allInstances, from: handler, croppedToInstancesExtent: false)
try CIContext().writePNGRepresentation(of: CIImage(cvPixelBuffer: buf), to: URL(fileURLWithPath: a[2]), format: .RGBA8, colorSpace: CGColorSpace(name: CGColorSpace.sRGB)!)
